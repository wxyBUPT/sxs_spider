#coding=utf-8
__author__ = 'xiyuanbupt'
import os.path

import tornado.web
import tornado.httpserver
import tornado.ioloop
import tornado.options
from motor.motor_tornado import MotorClient

from tornado.options import define,options
define("port",default=8000,help=u'接收请求的端口，默认为8000',type=int)

from m_interact.settings import Settings
from m_interact.urls import urlpatterns

class Application(tornado.web.Application):
    def __init__(self):
        handlers = urlpatterns
        conn = MotorClient(Settings.MONGO_HOST,Settings.MONGO_PORT)
        self.db = conn[Settings.DB_NAME]
        settings = dict(
            template_path = Settings.TEMPLATE_PATH,
            static_path = Settings.STATIC_PATH,
            debug = Settings.DEBUG,
        )
        tornado.web.Application.__init__(self,handlers=handlers,**settings)

def make_app():
    return Application()

def run():
    tornado.options.parse_command_line()
    app = make_app()
    app.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()

if __name__ == "__main__":
    run()
