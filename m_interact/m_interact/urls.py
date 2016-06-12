#coding=utf-8
from __future__ import absolute_import
__author__ = 'xiyuanbupt'

from .feedBack import HandleXMLYRe,FeedBack,HandleKLRe,ViewSummary


#在urlpatterns 中添加新的路由
urlpatterns = [
    (r'/infoCrawler',FeedBack),
    (r'/toCNR/xmly/(\w+)',HandleXMLYRe),
    (r'/toCNR/kl/(\w+)',HandleKLRe),
    #对内的统计页面，资源整体情况描述
    (r'/toStatistic/summary/',ViewSummary)
]
