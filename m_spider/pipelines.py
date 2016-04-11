# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import logging
import pymongo
from scrapy.pipelines.files import FilesPipeline
from scrapy.pipelines.images import ImagesPipeline
import scrapy

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
        #将具体的数据保存到 mongo 中
        try:
            self.db[item.collection].insert(dict(item))
            logging.info(u'新增一条%sitem 到mongo 中'%(item.s_type))
        except:
            logging.error(u'数据未能保存到mongod 中')
        finally:
            return item

