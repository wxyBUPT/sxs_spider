#coding=utf-8
from __future__ import absolute_import
import scrapy
from scrapy.http import Request
from ..items import QingtingAlbum,QTAudio
import datetime
from scrapy.utils.project import get_project_settings

settings = get_project_settings().get('QINGTINGCONF')
'''configure_logging(install_root_handler=False)
logging.basicConfig(
    filename= settings['logfile'],
    filemode = 'a',
    format = '%(asctime)s[%(levelname)s] %(message)s',
    level=logging.DEBUG
)'''


class QingtingSpider(scrapy.Spider):
	name = "qingting"

	def __init__(self):
		self.allowed_domains = settings['allowdomains']
		self.start_urls = settings['start_urls']
		self.playPR = settings['playPR']
		self.custom_settings = settings['qt_c_settings']
		super(QingtingSpider, self).__init__()

	def parse(self, response):
		for url in response.xpath('//div[@data-category="507"]/div/div/a'):
			category1 = url.xpath('div/div[2]/h5/text()').extract()[0]
			next_url = self.start_urls[0] + url.xpath('@data-switch-url').extract()[0]
			yield Request(next_url, meta = {'category1': category1}, callback = self.parse_second)

	def parse_second(self, response):
		for url in response.xpath('//div[@class="supervcategory subpage-wrapper clearfix"]/div[2]/div[position() <= last() - 1]'):
			category2 = url.xpath('div[1]/div[2]/div/text()').extract()[0]
			response.meta['category2'] = category2
			next_url = self.start_urls[0] + url.xpath('div[1]/div[2]/a/@data-switch-url').extract()[0]
			yield Request(next_url, meta = response.meta, callback = self.parse_third)

	def parse_third(self, response):
		for url in response.xpath('//div[@class="channels"]/ul/li'):
			title = url.xpath('div[1]/a/span/text()').extract()[0]
			response.meta['title'] = title
			next_url = self.start_urls[0] + url.xpath('div[1]/a/@data-switch-url').extract()[0]
			yield Request(next_url, meta = response.meta, callback = self.parse_fourth)

	def parse_fourth(self, response):
		item = QingtingAlbum()
		item['contentSource'] = "www.qingting.fm"
		item['crawlType'] = "qt_album"
		item['category'] = response.meta['category1']
		item['subcategory'] = response.meta['category2']
		item['albumName'] = response.xpath('//div[@class="channel-name"]/text()').extract()[0]
		item['albumPicUrl'] = response.xpath('//div[@class="cover"]/img/@src').extract()[0]
		item['albumPicPath'] = ''
		desc = response.xpath('//div[@class="abstract clearfix"]/div[2]/text()').extract()
		if len(desc) == 0:
			item['fullDescs'] = 'None'
		else:
			item['fullDescs'] = desc[0]
		item['crawlTime'] = str(datetime.datetime.now())[0:19]
		item['audios'] = []

		for content in response.xpath('//ul[@class="programs"]/li'):
			aname = content.xpath('div[2]/span/text()').extract()
			temp = QTAudio()
			temp['category_title'] = item['category']
			temp['sub_category_title'] = item['subcategory']
			temp['album_title'] = item['albumName']
			if len(aname) == 0:
				temp['audioName'] = 'None'
			else:
				temp['audioName'] = aname[0]
			audioUrls =  eval(content.xpath('@data-play-info').extract()[0])
			temp['playUrl'] = self.playPR + audioUrls['urls'][0]
			yield temp
			item['audios'].append(temp.copy())

		yield item

	def inspect(self,respons):
		from scrapy.shell import inspect_response
		inspect_response(respons,self)

