#coding=utf-8
__author__ = 'xiyuanbupt'
from m_interact.feedBack import FeedBack

#在urlpatterns 中添加新的路由
urlpatterns = [
    (r'/infoCrawler',FeedBack)
]
