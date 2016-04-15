#coding=utf-8
__author__ = 'xiyuanbupt'

import tornado.web
import tornado.httpserver
import tornado.ioloop
import tornado.options
import os.path

from tornado.options import define,options
define("port",default=8000,help=u'接收请求的端口，默认为8000',type=int)

from m_interact.settings import Settings
from m_interact.urls import urlpatterns

class Application(tornado.web.Application):
    def __init__(self):
        handlers = urlpatterns
        settings = dict(
            template_path = Settings.TEMPLATE_PATH,
            static_path = Settings.STATIC_PATH,
            debug = Settings.DEBUG,
        )
        tornado.web.Application.__init__(self,handlers=handlers,**settings)

def make_app():
    return Application()

if __name__ == "__main__":
    tornado.options.parse_command_line()
    app = make_app()
    app.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()
