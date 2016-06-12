#coding=utf-8
from __future__ import absolute_import
__author__ = 'xiyuanbupt'
import os.path

'''
数据推送接口与反馈接口与统计接口的配置文件
'''

#MONGO_URI = "mongodb://user:password@host:port/db_name"
MONGO_HOST = '114.112.103.33'
MONGO_PORT = 27017
DB_NAME = 'w_spider'
XMLY_ALBUM_DB = 'xmly_album'
KL_ALBUM_DB = 'kl_album'
QT_ALBUM = 'qt_item'
XMLY_AUDIO_COLLECTION_NAME= 'xmly_audio'
QT_AUDIO_COLLECTION_NAME = 'qt_audio'
KL_AUDIO_COLLECTION_NAME = 'kl_audio'
CRONTAB_RESULT_COLLECTION_NAME = 'crontab_result'

CRAWLED_INFO_DB = 'crawled_info_db'

TEMPLATE_PATH = os.path.join(os.path.dirname(__file__),"templates")
STATIC_PATH = os.path.join(os.path.dirname(__file__),"static")

DEBUG = True



class Settings:

    MONGO_HOST = MONGO_HOST
    MONGO_PORT = MONGO_PORT
    TEMPLATE_PATH = TEMPLATE_PATH
    STATIC_PATH = STATIC_PATH
    DEBUG = DEBUG
    QT_ALBUM = QT_ALBUM
    KL_ALBUM_DB = KL_ALBUM_DB
    XMLY_ALBUM_DB = XMLY_ALBUM_DB
    DB_NAME = DB_NAME
    CRAWLED_INFO_DB = CRAWLED_INFO_DB
    XMLY_AUDIO_COLLECTION_NAME = XMLY_AUDIO_COLLECTION_NAME
    QT_AUDIO_COLLECTION_NAME = QT_AUDIO_COLLECTION_NAME
    KL_AUDIO_COLLECTION_NAME = KL_AUDIO_COLLECTION_NAME
    CRONTAB_RESULT_COLLECTION_NAME = CRONTAB_RESULT_COLLECTION_NAME
