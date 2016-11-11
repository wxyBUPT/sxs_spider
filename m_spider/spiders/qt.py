# -*- coding: utf-8 -*-
from __future__ import absolute_import

import datetime
import json

import scrapy
from scrapy.http import Request
from scrapy import signals
from scrapy.xlib.pydispatch import dispatcher

from ..items import QingtingAlbum,QTAudio


class QtSpider(scrapy.Spider):
    name = "qt"
    allowed_domains = ["qingting.fm"]
    start_urls = (
        'http://www.qingting.fm/',
    )

    def __init__(self,stats,*args,**kwargs):
        dispatcher.connect(
            self.spider_closed,signals.spider_closed
        )
        super(QtSpider,self).__init__(*args,**kwargs)
        self.stats = stats

    @classmethod
    def from_crawler(cls, crawler, *args, **kwargs):
        spider = cls(crawler.stats,*args,**kwargs)
        spider._set_crawler(crawler)
        return spider

    def parse(self, response):
        urls = response.xpath('//div[@data-category="507"]/div/div/a');
        for url in urls:
            
            category = url.xpath('div/div[2]/h5/text()').extract()[0]
            next_url = 'http://www.qingting.fm' + url.xpath('@data-switch-url').extract()[0]
            self.logger.info(u"Category: 开始爬取类别%s"%category)
            yield Request(next_url,meta={'category':category},callback=self.parse_category)


    def inspect(self,response):
        from scrapy.shell import inspect_response
        inspect_response(response,self)

    def parse_category(self,response):
        divs = response.css('.category')[:-1]
        for div in divs:
            sub_category = div.css('.title').xpath('text()').extract()[0]
            self.logger.info(u"SubCategory: 开始爬取类别:%s的子类别:%s"%(response.meta['category'],sub_category))
            # 对应更多album
            more_album_url = 'http://www.qingting.fm'  + div.css('.more').xpath('@data-switch-url').extract()[0]
            response.meta['sub_category'] = sub_category
            yield Request(more_album_url,meta=response.meta,callback=self.parse_more_category)

    def parse_more_category(self,response):
        lis = response.css('.playable')
        for li in lis:
            self.stats.inc_value(u"Category_%s_%s_album_counts"%(response.meta['category'],response.meta['sub_category']),1,0)
            title = li.xpath('div[1]/a/span/text()').extract()[0]
            album_url = 'http://www.qingting.fm' + li.xpath('div[1]/a/@data-switch-url').extract()[0]
            response.meta['title'] = title
            yield Request(album_url,meta=response.meta,callback=self.parse_album)

    def parse_album(self,response):
        album = QingtingAlbum()
        album['contentSource'] = 'www.qingting.fm'
        album['crawlType'] = 'qt_album'
        album['category'] = response.meta['category']
        album['subcategory'] = response.meta['sub_category']
        album['albumName'] = response.css('.channel-name').xpath('text()').extract()[0]
        album['albumPicUrl'] = response.css('.cover').xpath('img/@src').extract()[0]
        desc = response.css('.abstract').xpath('div/text()')[-1].extract()
        album['fullDescs'] = desc if desc is not None else 'None'
        album['crawlTime'] = datetime.datetime.now()
        album['audios'] = []
        album['albumUrl'] = response.url

        playables = response.css('.playable')
        for playable in playables:
            audio_info = json.loads(playable.xpath('@data-play-info').extract()[0])
            audio = QTAudio()
            audio['category_title'] = album['category']
            audio['sub_category_title'] = album['subcategory']
            audio['album_title'] = album['albumName']
            audio['audioName'] = audio_info['name']
            audio['playUrl'] = 'http://od.qingting.fm' + audio_info['urls'][0]
            self.stats.inc_value("Audio_count",1,0)
            yield audio
            album['audios'].append(audio.copy())
        self.stats.inc_value("Album_count",1,0)
        yield album

    def spider_closed(self):
        stats = self.stats
        print stats.get_stats()
        from m_spider.util.report import write_qt_status
        self.logger.info(u'完成爬取，保存报表')
        write_qt_status(stats.get_stats())
