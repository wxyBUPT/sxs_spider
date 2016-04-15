#coding=utf-8
from __future__ import absolute_import
__author__ = 'xiyuanbupt'

import pymongo

from .settings import Settings

mongoClient = pymongo.MongoClient(Settings.MONGO_URI)
db = mongoClient[Settings.DB_NAME]

def singleton(cls):
    instance = cls()
    instance.__call__ = lambda: instance
    return instance

@singleton
class XMLYUtil():
    '''
    xmly
    '''
    def __init__(self):
        self.album = db[Settings.XMLY_ALBUM_DB]

    def getAlbumCount(self):
        '''
        获得xmly 中album 的总数
        :return:
        '''
        return self.album.count()

    def getAuidoCount(self):
        '''
        获得xmly 中audio 的数量
        :return:
        '''
        cursor = self.album.aggregate(
            [
                {
                    "$project":{"numberOfAudios":{"$size":"$audios"}}
                },
                {
                    "$group":{
                        "_id":"null",
                        "total":{"$sum":"$numberOfAudios"}
                    }
                }
            ]
        )
        return cursor.next()['total']

@singleton
class KLUtil():
    '''
    kl
    '''
    def __init__(self):
        self.album = db[Settings.KL_ALBUM_DB]

    def getAlbumCount(self):
        return self.album.count()

    def getAudioCount(self):
        cursor = self.album.aggregate((
            [
                {
                    "$project":{"numberOfAudios":{"$size":"$audios"}}
                },
                {
                    "$group":{
                        "_id":"null",
                        "total":{"$sum":"$numberOfAudios"}
                    }
                }
            ]
        ))
        return cursor.next()['total']

@singleton
class QTUtil():
    '''
    qt
    '''
    def __init__(self):
        self.album = db[Settings.QT_ALBUM]

    def getAlbumCount(self):
        return self.album.count()

    def getAudioCount(self):
        cursor = self.album.aggregate((
            [
                {
                    "$project":{"numberOfAudios":{"$size":"$audios"}}
                },
                {
                    "$group":{
                        "_id":"null",
                        "total":{"$sum":"$numberOfAudios"}
                    }
                }
            ]
        ))
        return cursor.next()['total']

@singleton
class CrawledInfoGetter:
    '''
    统计，获取与存储爬取相关信息的工具类
    '''
    def __init__(self):
        self.crawledInfo = db[Settings.CRAWLED_INFO_DB]


