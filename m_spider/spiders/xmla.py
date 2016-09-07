# -*- coding: utf-8 -*-
from __future__ import absolute_import
import urlparse
import datetime

import scrapy
import requests
from scrapy.selector import Selector
from scrapy.utils.project import get_project_settings

from ..items import XMLYCategory,XMLYAlbum,XMLYAudio,XMLYAlbumMeta


class XmlaSpider(scrapy.Spider):
    name = "xmly"
    allowed_domains = ["ximalaya.com"]
    baseUrl = 'http://www.ximalaya.com'

    headers = {
        "Host":"www.ximalaya.com",
        "User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10.11; rv:44.0) Gecko/20100101 Firefox/44.0",
        "Accept":"application/json, text/javascript, */*; q=0.01",
        "Referer":"zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3",
    }
    start_urls = ('http://www.ximalaya.com/dq/all/',)

    # 所有有效的 category
    effectiveCategorys = (
        u'有声书',u'音乐',u'娱乐',u'相声评书',u'儿童',u'3D体验馆',
        u'脱口秀',u'资讯',u'情感生活',u'历史人文',u'外语',u'教育培训',
        u'名校公开课',u'百家讲坛',u'广播剧',u'戏曲',u'电台',u'商业财经',
        u'IT科技',u'健康养生',u'校园',u'汽车',u'旅游',u'电影',u'ACG'
    )
    globalSettings = get_project_settings()

    custom_settings = globalSettings.getdict("XMLY_SETTINGS")

    #从 start_urls 中产生各类别的首页地址
    def parse(self, response):
        categorys = response.css('.sort_list').xpath('li')
        tag_wrap = response.css(".tag_wrap")
        for category in categorys:
            xmly = XMLYCategory()
            try:
                cid = category.xpath('@cid').extract()[0]
                cname = category.xpath('@cname').extract()[0]
                href = category.xpath('a/@href').extract()[0]
                href = urlparse.urljoin(self.baseUrl,href)
                nameText = category.xpath('a/text()').extract()[0]
            except:
                break
            xmly['cid'] = cid
            xmly['cname'] = cname
            xmly['href'] = href
            xmly['nameText'] = nameText
            try:
                div = tag_wrap.css('div[data-cache="%s"]'%cid)
                sub = div.xpath('a/@tid').extract()
                xmly['subCategorys'] = sub
            except:
                pass
            if nameText in self.effectiveCategorys:
                yield xmly
                yield scrapy.Request(
                    href,callback=self.parse_category,headers=self.headers,
                    meta = {'dont_merge_cookies':True}
                )

    #生成每一个电台下对应的 album
    def parse_category(self,response):
        #不考虑只有一页的category
        pageInfo = response.css('.pagingBar_wrapper a')[-2]
        #下面代码处理 category 中的第一页内容
        self._parse_category(response)
        page = int(pageInfo.xpath('text()').extract()[0])
        url = response.url
        for i in range(2,page+1):
            i_url = urlparse.urljoin(url,str(i))
            yield scrapy.Request(
                i_url,callback=self._parse_category,
                headers=self.headers,
                meta={'dont_merge_cookies':True}
            )


    def _parse_category(self,response):
        '''
        获得category 中对应专辑的通用代码
        :param response:
        :return:
        '''
        album_items = response.css('div.discoverAlbum_item')
        for album in album_items:
            href = album.xpath('div/a/@href').extract()[0]
            albumId = album.xpath('@album_id').extract()[0]
            imgSrc = album.xpath('div/a/span/img/@src').extract()[0]
            albumName = album.xpath('div/a/span/img/@alt').extract()[0]
            playTime = album.xpath('div/div/span/text()').extract()[0]
            item = XMLYAlbumMeta()
            item['href'] = href
            item['album_id'] = albumId
            item['imgSrc'] = imgSrc
            item['album_name'] = albumName
            item['playTime'] = playTime
            meta = {
                "item":item,
                'dont_merge_cookies':True,
            }
            yield scrapy.Request(
                href,callback=self.parse_album,headers=self.headers,
                meta = meta
            )

    def parse_album(self,response):
        curBaseUrl = response.url
        item = response.meta['item']
        xmlyAl = XMLYAlbum()
        xmlyAl.update(item)

        xmlyAl['categoryName'] = response.css('.detailContent_category > a:nth-child(1)').xpath('text()').extract()[0]
        xmlyAl['uploadUserName'] = response.css('div.username').xpath('text()').extract()[0]
        uploaderUrl = response.css('li.nav_item:nth-child(1) > a:nth-child(1)').xpath('@href').extract()[0]
        uploaderUrl = urlparse.urljoin(self.baseUrl,uploaderUrl)
        xmlyAl['uploadUserUrl'] = uploaderUrl
        tags = response.css('a.tagBtn2').xpath('span/text()').extract()
        xmlyAl['tags'] = tags
        xmlyAl['albumDesc'] = ''.join(response.css('.mid_intro > article').xpath('text()').extract())
        audioCountsStr = response.css('.albumSoundcount').xpath('text()').extract()[0]
        audioCount = int(audioCountsStr[1:-1])

        audios = []
        #下面的代码负责获得各个audio 的相关信息
        #对应 album 第一页的所有 sounds
        #获得有多少页的信息
        pageCountInfo = response.css('.pagingBar_wrapper')
        pageInfo = pageCountInfo.xpath('a')
        try:
            pageCount = int(pageInfo[-2].xpath('text()').extract()[0])
        except:
            pageCount = 1

        soundsInfo = response.css('li[sound_id]')

        for s in soundsInfo:
            audio = XMLYAudio()
            try:
                a_id = s.xpath('@sound_id').extract()[0]
                created_at = s.xpath('div/div/span/text()').extract()[0]
                created_at = datetime.datetime.strptime(
                    created_at,"%Y-%m-%d"
                )
                audio["id"] = a_id
                audio["created_at"] = created_at
                audio['uploadUserName'] = xmlyAl['uploadUserName']
            except:
                pass
            a_url = "http://www.ximalaya.com/tracks/%s.json"%(a_id)
            r = requests.get(a_url,headers = self.headers)
            tmpDict = r.json()
            try:
                del tmpDict['discounted_price']
                del tmpDict['price']
                del tmpDict['id']
                del tmpDict['is_free']
                del tmpDict['waveform']
                del tmpDict['formatted_created_at']
                del tmpDict['is_favorited']
                del tmpDict['have_more_intro']
                del tmpDict['time_until_now']
                del tmpDict['played_secs']
                del tmpDict['is_paid']
            except:
                pass
            audio.update(tmpDict)
            yield audio
            audios.append(
                dict(
                    id = audio.get('id',None),
                    album_id = audio.get('album_id',None)
                )
            )

        for i in range(2,pageCount+1):
            tmpUrl = "%s?page=%s"%(curBaseUrl,i)
            res = requests.get(tmpUrl)
            se = Selector(text=res.content)
            ul = se.css('.album_soundlist > ul:nth-child(1)')
            soundsInfo = se.css('li[sound_id]')
            for s in soundsInfo:
                audio = XMLYAudio()
                try:
                    a_id = s.xpath('@sound_id').extract()[0]
                    created_at = s.xpath('div/div/span/text()').extract()[0]
                    created_at = datetime.datetime.strptime(
                        created_at,"%Y-%m-%d"
                    )
                    audio["id"] = a_id
                    audio["created_at"] = created_at
                    audio['uploadUserName'] = xmlyAl['uploadUserName']

                except:
                    pass
                a_url = "http://www.ximalaya.com/tracks/%s.json"%(a_id)
                r = requests.get(a_url,headers = self.headers)
                tmpDict = r.json()
                try:
                    del tmpDict['id']
                    del tmpDict['waveform']
                    del tmpDict['formatted_created_at']
                    del tmpDict['is_favorited']
                    del tmpDict['have_more_intro']
                    del tmpDict['time_until_now']
                    del tmpDict['played_secs']
                except:
                    pass
                audio.update(tmpDict)
                yield audio
                audios.append(dict(
                    id = audio.get('id',None),
                    album_id = audio.get('album_id',None)
                ))
            pass
        xmlyAl['audios'] = audios
        yield xmlyAl