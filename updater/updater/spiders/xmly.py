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
    settings = get_project_settings()
    store = settings.getdict("XMLY_STORE")

    def parse(self, response):
        pass
