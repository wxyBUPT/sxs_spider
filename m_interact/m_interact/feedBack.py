#coding=utf-8
from __future__ import absolute_import
__author__ = 'xiyuanbupt'

import tornado.web
import tornado.escape
from tornado import gen
from bson import json_util
import json

from m_interact.m_interact.settings import Settings


class FeedBack(tornado.web.RequestHandler):

    @gen.coroutine
    def get(self, *args, **kwargs):
        data = {
            'totalAlbumCount':10000,
            'totalAudioCount':100,
            'kl':{
                'albumCount':10,
                'audioCount':1000,
            }
        }
        self.set_header(
            'Content-Type','text/javascript'
        )
        self.write(
            tornado.escape.json_encode(data)
        )

class HandleXMLYRe(tornado.web.RequestHandler):
    '''
    负责处理喜马拉雅的回调函数
    '''

    @gen.coroutine
    def get(self, uuid):
        coll = self.application.db[Settings.XMLY_AUDIO_COLLECTION_NAME]
        audio = yield coll.find_one(
            {
                "uuid":uuid
            }
        )
        if audio == None:
            self.set_status(404,u'audioNotFount')
            self.finish(u"<html><body> Not Found</body></html>")
        else:
            self.set_header(
                'Content-Type','text/javascript'
            )
            self.write(
                json.dumps(audio,default=json_util.default)
            )

class HandleKLRe(tornado.web.RequestHandler):
    '''
    负责处理考拉网站的回调函数
    '''

    @gen.coroutine
    def get(self, uuid):
        coll = self.application.db[Settings.KL_AUDIO_COLLECTION_NAME]
        audio = yield coll.find_one(
            {
                "uuid":uuid
            }
        )
        if audio == None:
            self.set_status(404,u'audioNotFound')
            self.finish(u"<html><body> Not Found </body></html>")
        else:
            self.set_header(
                'Content-Type','text/javascript'
            )
            print audio
            self.write(
                json.dumps(audio,default=json_util.default)
            )

class ViewSummary(tornado.web.RequestHandler):
    '''
    内部统计页面地址
    '''
    @gen.coroutine
    def get(self,foo):
        '''
        返回时间区间内 summary 情况
        :param start_time:
        :param end_time:
        :return:
        '''
        coll = self.application.db[Settings.CRONTAB_RESULT_COLLECTION_NAME]
        latest = coll.find(
            {"type":"summary"}
        ).sort([("_id",1),]).limit(1)
        while (yield latest.fetch_next):
            doc = latest.next_object()
            break
        del doc['_id']
        self.write(doc)