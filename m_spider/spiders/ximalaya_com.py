# -*- coding: utf-8 -*-
import scrapy


class XimalayaComSpider(scrapy.Spider):
    name = "ximalaya.com"
    allowed_domains = ["ximalaya.com"]
    start_urls = (
        'http://www.ximalaya.com/dq/all/',
    )

    def parse(self, response):
        print response.url
        pass
