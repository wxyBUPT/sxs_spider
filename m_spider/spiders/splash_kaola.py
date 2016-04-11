# -*- coding: utf-8 -*-
__author__ = 'xiyuanbupt'
import scrapy
from scrapy.http.headers import Headers
import json

RENDER_HTML_URL = "http://192.168.99.100:8050/render.html"

class SplashKaolaSpider(scrapy.Spider):
    name = "splash_kaola"
    allowed_domains = ["kaolafm.com"]
    start_urls = (
        'http://www.kaolafm.com/category/32',
        'http://www.kaolafm.com/zj/Xndk2o2g.html'
    )

    def start_requests(self):
        headers = Headers(
            {
                'User-Agent':"Mozilla/5.0 (Macintosh; Intel Mac OS X 10.11; rv:44.0) Gecko/20100101 Firefox/44.0",
                'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',

            }
        )
        for url in self.start_urls:
            yield scrapy.Request(url, self.parse, headers=headers, meta={
                'splash': {
                    'endpoint': 'render.html',
                    'args': {'wait': 0.5},
                }
            })

    def parse(self, response):
        print u'done'
        from scrapy.shell import inspect_response
        inspect_response(response,self)
        pass