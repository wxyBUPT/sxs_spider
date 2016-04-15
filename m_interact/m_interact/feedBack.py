#coding=utf-8
__author__ = 'xiyuanbupt'

import tornado.web
import tornado.escape

class FeedBack(tornado.web.RequestHandler):

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

