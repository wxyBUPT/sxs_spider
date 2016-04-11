# -*- coding: utf-8 -*-
import scrapy


class XmlyUpdaterSpider(scrapy.Spider):
    name = "xmly_updater"
    allowed_domains = ["ximalaya.com"]
    start_urls = (
        'http://www.ximalaya.com/',
    )

    def parse(self, response):
        pass
