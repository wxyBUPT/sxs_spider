# -*- coding: utf-8 -*-
from __future__ import absolute_import
import scrapy
from scrapy.utils.project import get_project_settings

from dbTool.tool import XMLYUtil
xmlyUtil = XMLYUtil()
class XmlySpider(scrapy.Spider):
    name = "xmly"
    allowed_domains = ["ximalaya.com"]
    start_info = xmlyUtil.getAllAlbumUrlWithCrawledAudiosInfo()
    custom_settings = get_project_settings(
    ).getdict("XMLY_SETTINGS")
    def start_requests(self):
        allAlbum = xmlyUtil.getAllAlbumUrlWithCrawledAudiosInfo()
        for album in  allAlbum:
            #对返回的数据进行预处理
            meta = {}
            #在mongog 中的 _id
            meta['album_id'] = album['_id']
            meta['albumHref'] = album['href']
            #通过id 唯一表示当前是否最新的内容
            meta['audioId'] = set(
                audio['id'] for audio in album['audios']
            )
            yield scrapy.Request(
                album['href'],meta=meta
            )
            #如下代码用于调试执行
            break

    def parse(self, response):
        audios  = response.css('.album_soundlist ul li')
        visitedIdSet = response.meta['audioId']
        allAudioNotVisited = True
        for audio in audios:
            sound_id = audio.xpath('@sound_id').extract()[0]
            if sound_id in visitedIdSet:
                allAudioNotVisited = False
            else:
                #访问未被访问到的地址
                pass

        print response.meta

        from scrapy.shell import inspect_response
        inspect_response(response,self)
        pass
