# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import uuid
import logging
import datetime
import pymongo
from scrapy.pipelines.files import FilesPipeline
from scrapy.pipelines.images import ImagesPipeline
import scrapy
from datetime import date

class MSpiderPipeline(object):
    def process_item(self, item, spider):
        return item


#lass saveToMongo(object):

#   def __init__(self,mongo_uri,mongo_db):
#       self.mongo_uri = mongo_uri
#       self.mongo_db = mongo_db

#   @classmethod
#   def from_crawler(cls,crawler):
#       return cls(
#           mongo_uri = crawler.settings.get('MONGO_URI'),
#           mongo_db = crawler.settings.get('MONGO_DATABASE','w_spider')
#       )

#   def open_spider(self,spider):
#       self.client = pymongo.MongoClient(self.mongo_uri)
#       self.db = self.client[self.mongo_db]

#   def close_spider(self,spider):
#       self.client.close()

#   def process_item(self,item,spider):
#       #将具体的数据保存到 mongo 中
#       pass


#将图片存储到本地，并为 item 添加相应的字段
#并需要借助于redis 来去重
#
class KlimageDownloader(ImagesPipeline):


    def get_media_requests(self, item, info):
        if item.s_type == 'kl_category':
            pass
        elif item.s_type == 'kl_album':
            return self._get_kl_album_requests(item,info)
        else:
            pass

    def item_completed(self, results, item, info):
        if item.s_type=='kl_category':
            pass
        elif item.s_type == 'kl_album':
            item['albumPics'] = results
        else:
            pass
        return item

    def _get_kl_album_requests(self,item,info):
        albumPicUrl = item['albumPicUrl']
        try:
            yield scrapy.Request(albumPicUrl)
        except:
            logging.error(u'get albumPicUrl : %s fail'%(albumPicUrl))
        for audio in item['audios']:
            try:
                url = audio['audioPicUrl']
                yield scrapy.Request(url)
            except:
                logging.error(
                    u'get audioPicUrl %s fail'%(url)
                )

class KlAudioDownloader(FilesPipeline):
    def get_media_requests(self, item, info):
        if item.s_type == 'kl_album':
            return self._get_kl_album_requests(item,info)

    def _get_kl_album_requests(self,item,info):
        for audio in item['audios']:
            try:
                yield scrapy.Request(audio['playUrl'])
                yield scrapy.Request(audio['mp3PlayUrl'])
                # yield scrapy.Request(audio['accPlayUrl'])
                yield scrapy.Request(audio['m3u8PlayUrl'])
            except:
                logging.error(
                    u'send audio request fail: playUrl %s,'
                    u'mp3PlayUrl %s, m3u8PlayUrl%s'%(
                        audio['playUrl'],audio['mp3PlayUrl'],
                        audio['m3u8PlayUrl']
                    )
                )
            finally:
                pass
    def item_completed(self, results, item, info):
        if item.s_type == 'kl_album':
            item['albumSounds'] = results
        return item

class XmlyImageDownloader(ImagesPipeline):

    def get_media_requests(self, item, info):
        if item.s_type == 'xmly_album':
            return self._get_xmly_album_requests(item,info)


    def _get_xmly_album_requests(self,item,info):
        yield scrapy.Request(item['imgSrc'])
        for audio in item['audios']:
            try:
                yield scrapy.Request(audio['cover_url'])
                yield scrapy.Request(audio['cover_url_142'])
            except:
                logging.error(u'get cover_url requests failed'
                              u'couver_url:%s,'
                              u'cover_url_142%s'%(
                    audio['cover_url'],
                    audio['cover_url_142']
                ))

    def item_completed(self, results, item, info):
        if item.s_type == 'xmly_album':
            item['audiosImages'] = results
        return item

class XmlyAudiosDownloader(FilesPipeline):

    def get_media_requests(self, item, info):
        if item.s_type == 'xmly_album':
            return self._get_xmly_album_requests(item,info)


    def _get_xmly_album_requests(self,item,info):
        for audio in item['audios']:
            yield scrapy.Request(audio['play_path_64'])
            yield scrapy.Request(audio['play_path_32'])
            yield scrapy.Request(audio['play_path'])
    def item_completed(self, results, item, info):
        if item.s_type == 'xmly_album':
            item['audiosFiles'] = results
        return item

class SaveToMongo(object):

    def __init__(self,mongo_uri,mongo_db):
        self.mongo_uri = mongo_uri
        self.mongo_db = mongo_db
        self.now = None

    @classmethod
    def from_crawler(cls,crawler):
        return cls(
            mongo_uri = crawler.settings.get('MONGO_URI'),
            mongo_db = crawler.settings.get('MONGO_DATABASE','w_spider')
        )

    def open_spider(self,spider):
        self.client = pymongo.MongoClient(self.mongo_uri)
        self.db = self.client[self.mongo_db]

    def close_spider(self,spider):
        self.client.close()

    def process_item(self,item,spider):
        #将每天爬取的数量保存到mongo中
        self.now = str(date.today())
        #将具体的数据保存到 mongo 中
        s_type = item.s_type
        if s_type == 'xmly_audio':
            self._saveXMLYAudio(item)
        elif s_type == 'xmly_album':
            self._saveXMLYAlbum(item)
        elif s_type == 'kl_audio':
            self._saveKLAudio(item)
        elif s_type == 'kl_album':
            self._saveKlAlbum(item)
        elif s_type == 'qt_item':
            self._saveQTAlbum(item)
        elif s_type == 'qt_audio':
            self._saveQTAudio(item)
        else:
            self.db[s_type].insert(dict(item))

    def _saveQTAlbum(self,item):
        key =  'album' + self.now
        self.db['qt_daily'].update(
            {
                'key':key,
            },
            {
                "$inc":{"crawledCount":1}
            },
            {
                "upsert":True
            }
        )
        album = self.db[item.collection].find_one(
            {
                "category":item["category"],
                "subcategory":item["subcategory"],
                "albumName":item["albumName"]
            }
        )
        if album:
            self.db[item.collection].update(
                {
                    "_id":album['_id']
                },
                {
                    "$inc":{"crawledCount":1}
                }
            )
        else:
            tmp = dict(item)
            tmp['crawledCount'] = 1
            tmp['crawledTime'] = datetime.datetime.now()
            self.db[item.collection].insert(
                tmp
            )
        return item

    def _saveQTAudio(self,item):
        key = 'audio' + self.now
        self.db['qt_daily'].update(
            {
                'key':key,
            },
            {
                "$inc":{"crawledCount":1}
            },
            {
                "upsert":True
            }
        )
        audio = self.db[item.collection].find_one(
            {
                "audioName":item["audioName"],
                "playUrl":item["playUrl"]
            }
        )
        if audio:
            self.db[item.collection].update(
                {
                    "_id":audio["_id"]
                },
                {
                    "$inc":{"crawledCount":1}
                }
            )
        else:
            tmp = dict(item)
            tmp['crawledCount'] = 1
            tmp['uuid'] = uuid.uuid1().hex
            tmp['crawledTime'] = datetime.datetime.now()
            tmp['sendToCNRTime'] = None
            tmp['audioDownloadDir'] = None
            self.db[item.collection].insert(
                tmp
            )
        return item

    def _saveKLAudio(self,item):
        key = 'audio' + self.now
        self.db['kl_daily'].update(
            {
                'key':key,
            },
            {
                "$inc":{"crawledCount":1}
            },
            {
                "upsert":True
            }
        )
        #以audioId 与 playUrl 为主键更新或者插入数据
        audio = self.db[item.collection].find_one(
                {
                    'audioId':item["audioId"],
                    'playUrl':item['playUrl']
                }
        )
        if audio:
            self.db[item.collection].update(
                {
                    "_id":audio['_id']
                },
                {
                    "$inc":{"crawledCount":1},
                    "$set":dict(
                        likedNum = item['likedNum'],
                        listenNum = item['listenNum'],
                        commentNum = item['commentNum']
                    )
                }
            )
        else:
            tmp = dict(item)
            tmp['crawledCount'] = 1
            tmp['uuid'] = uuid.uuid1().hex
            tmp['crawledTime'] = datetime.datetime.now()
            tmp['sendToCNRTime'] = None
            tmp['audioDownloadDir'] = None
            self.db[item.collection].insert(
               tmp
            )
        return item

    def _saveKlAlbum(self,item):
        key = 'album' + self.now
        self.db['kl_daily'].update(
            {
                'key':key,
            },
            {
                "$inc":{"crawledCount":1}
            },
            {
                "upsert":True
            }
        )
        album = self.db[item.collection].find_one(
            {
                'categoryId':item['categoryId'],
                'albumId' : item['albumId']
            }
        )
        #更新本专辑被爬取的次数
        if album:
            self.db[item.collection].update(
                {
                    '_id':album['_id']
                },
                {
                    '$inc':{'crawledCount':1},
                    '$set':dict(item)
                }
            )
        else:
            tmp = dict(item)
            tmp['crawledCount'] = 1
            tmp['crawledTime'] = datetime.datetime.now()
            self.db[item.collection].insert(
                dict(item)
            )
        return item

    def _saveXMLYAudio(self,item):
        key = 'audio' + self.now
        self.db['xmly_daily'].update(
            {
                'key':key,
            },
            {
                "$inc":{"crawledCount":1}
            },
            {
                "upsert":"true"
            }
        )
        audio = self.db[item.collection].find_one(
            {
                'album_id':item['album_id'],
                'id':item['id']
            }
        )
        if not audio:
            tmp = dict(item)
            tmp['crawledCount'] = 1
            tmp['uuid'] = uuid.uuid1().hex
            tmp['crawledTime'] = datetime.datetime.now()
            tmp['audioDownloadDir'] = None
            tmp['sendToCNRTime'] = None
            tmp['audioChecksum'] = None
            self.db[item.collection].insert(tmp)
        else:
            self.db[item.collection].update(
                {
                    '_id':audio['_id']
                },
                {
                    "$inc":{'crawledCount':1},
                    "$set":dict(item)
                }
            )
        return item

    def _saveXMLYAlbum(self,item):
        key = 'album' + self.now
        self.db['xmly_daily'].update(
            {
                'key':key,
            },
            {
                "$inc":{"crawledCount":1}
            },
            {
                "upsert":"true"
            }
        )
        album = self.db[item.collection].find_one(
            {
                'album_id':item['album_id']
            }
        )
        if not album:
            tmp = dict(item)
            tmp['crawledCount'] = 1
            tmp['crawledTime'] = datetime.datetime.now()
            self.db[item.collection].insert(tmp)
        else:
            self.db[item.collection].update(
                {
                    '_id':album['_id'],
                },
                {
                    '$inc':{'crawledCount':1},
                    "$set":dict(item)
                }
            )
        return item
