#coding=utf-8
from __future__ import absolute_import
'''
对于删除文件的操作仅仅在服务器端执行有效
'''

from itertools import chain
from os import path
import os
from os.path import getsize

from pymongo import MongoClient
from conf_util import ConfUtil

from m_spider.settings import XMLY_SETTINGS
client = MongoClient(ConfUtil.getMongoIP(),ConfUtil.getMongoPort())

#喜马拉雅中的一些查询函数
class XMLYUtil():
    '''
    基于数据库统计xmly 目前资源的情况
    '''
    imagesDir = XMLY_SETTINGS['IMAGES_STORE']
    filesDir = XMLY_SETTINGS['FILES_STORE']
    def __init__(self):
        db = client[ConfUtil.getDBName()]
        self.album = db[ConfUtil.getXMLYAlbumCollectionName()]
        self.category = db[ConfUtil.getXMLYCategoryCollectionName()]

    def getAllAudioIdFormAlbum(self,album):
        albumId = album['album_id']
        audios = album['audios']
        idList = []
        for audio in audios:
            id = audio['id']
            idList.append(id)
        return idList

    def getAllAudioId(self):
        '''
        获得所有音频的id
        :return:
        '''
        allAlbum = self.album.find({})
        allAudioId = []
        for album in allAlbum:
            allAudioId += self.getAllAudioIdFormAlbum(album)
        return allAudioId

    def isAudioInAlbum(self,albumId,audioId):
        '''
        根据 albumId 以及audioId 判断album 中是否包含这个audio
        :param albumId:string
        :param audioId:string
        :return:
        '''
        try:
            tmp = self.album.find_one({
                "album_id":albumId,"audios.id":audioId
            })
            if tmp == None:
                return False
            else:
                return True
        except:
            return False

    def getAlbumCount(self):
        '''
        获得xmly 中的album 总数
        :return:
        '''
        return self.album.count()

    def getAllCategoryWithCount(self):
        '''
        获得所有类别与相应的album 数量
        :return:
        '''
        cursor = self.album.aggregate(
            [
                {
                    '$group':{
                        "_id":{"categoryName":"$categoryName"},
                        "count":{"$sum":1}
                    }
                },
            ]
        )
        return {
            i['_id']['categoryName']:i['count'] for i in cursor
        }

    def getTotalAudioCount(self):
        '''
        获得audio 的总数
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

    def _findInfoFromAlbumByUrl(self,album,url):
        audioFiles = album['audiosFiles']
        audioImages = album['audiosImages']
        for info in iter(audioFiles+audioImages):
            if info[1]['url'] == url:
                return info[1]
        return None

    def _getAudiosFromAlbum(self,album):
        '''
        从相应的album 中获得所有audios 相关的信息
        :param album:
        :return:
        '''
        def _findByUrl(url):
            return self._findInfoFromAlbumByUrl(album,url)

        audios = album['audios']
        for audio in audios:
            audio['cover_url_142'] = _findByUrl(audio['cover_url_142'])
            audio['play_path'] = _findByUrl(audio['play_path'])
            audio['cover_url'] = _findByUrl(audio['cover_url'])
            audio['paly_path_32'] = _findByUrl(audio['play_path_32'])
            audio['play_path_64'] = _findByUrl(audio['play_path_64'])
            yield audio

    def getAllAudio(self):
        '''
        获得所有的audio，以iterator 形式返回
        执行一次比较耗费资源，慎重使用
        '''
        cursor = self.album.find({})
        for album in cursor:
            return self._getAudiosFromAlbum(album)

    def getAllAlbumUrlWithCrawledAudiosInfo(self):
        '''
        获得所有 album 的url 地址
        '''
        cursor = self.album.find(
            {},
            {
                "audios":1,
                "href":1,
            }
        )
        for album in cursor:
            yield album

    def addNewAudio(self,_id,audios,audiosFiles,audioImages):
        '''
        向 album 中添加新的 audios
        各个参数都未数组形式
        '''
        self.album.update(
            {"_id":_id},
            {
                "$set":{
                    "$push":{
                        "audios":{"$each":audios},
                        "audiosFiles":{"$each":audiosFiles},
                        "audiosImages":{"$each":audioImages}

                    }
                }
            }
        )

    def getAlbumById(self,_id):
        return self.album.find_one(
            {
                "_id":_id
            }
        )

    def deleteAlbumWithFiles(self,_id):
        '''
        安全删除，删除album 与对应的文件
        '''
        album = self.album.find_and_modify(
            query={"_id":_id},
            update=None,
            remove=True
        )
        try:
            for image in album['audiosImages']:
                baseDir = image[1]['path']
                imagePath = path.join(self.imagesDir,baseDir)
                try:
                    os.remove(imagePath)
                except OSError:
                    pass

            for audio in album['audiosFiles']:
                baseDir = audio[1]['path']
                audioPath = path.join(self.filesDir,baseDir)
                try:
                    os.remove(audioPath)
                except OSError:
                    pass
        except:
            #如果删除失败，则重新插入
            print u'删除失败'
            self.album.insert(
                album
            )

    def getAlbumDiskSize(self,_id):
        '''
        获得某个album 文件总打下
        '''
        album = self.album.find_one(
            {"_id":_id}
        )
        totalSize = 0.0
        for image in album['audiosImages']:
            baseDir = image[1]['path']
            imagePath = path.join(self.imagesDir,baseDir)
            try:
                size = getsize(imagePath)
                totalSize += size/1024
            except:
                pass

        for audio in album['audiosFiles']:
            baseDir = audio[1]['path']
            audioPath = path.join(self.filesDir,baseDir)
            try:
                size = getsize(audioPath)
                totalSize += size/1024
            except:
                pass
        return totalSize

    def getAllAlbumByCategory(self,categoryName,count = None):
        '''
        通过 category 的名字获得所有的 album
        '''
        with self.album.find(
                {'categoryName':categoryName}
        ) as cursor:
            if count == None:
                for album in cursor:
                    yield album
            else:
                count = int(count)
                while(count != 0 ):
                    count -= 1
                    yield cursor.next()

class IndexUtil:
    '''
    所有执行索引的命令，只执行一次
    '''
    @classmethod
    def createXMLYAlbumIndex(cls):
        '''
        为xmly 的album 创建索引
        :return:
        '''
        pass





