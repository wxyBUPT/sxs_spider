#coding=utf-8

__author__ = 'xiyuanbupt'
from dbTool.tool import XMLYUtil,QTUtil,KLUtil
from cron.m_cron import getSummary
import datetime

from unittest import TestCase
import  unittest
from pprint import pprint
import json

from bson.objectid import ObjectId
from pymongo import MongoClient
from conf_util import ConfUtil
client = MongoClient(ConfUtil.getMongoIP(),ConfUtil.getMongoPort())
db = client[ConfUtil.getDBName()]


import crawlManage
#http://www.ximalaya.com/16981310/album/374729
#被用于测试使用
class TestXMLYUtil(unittest.TestCase):
    xmlyUtil = XMLYUtil()

    def testGetAllAudioId(self):
        pass

#   def testIsAudioInAlbum(self):
#       self.assertTrue(
#           self.xmlyUtil.isAudioInAlbum(
#               "3249896","10199421"
#           )
#       )
#       self.assertFalse(
#           self.xmlyUtil.isAudioInAlbum(
#               "3249896","11111111"
#           )
#       )

    def testGetAlbumCount(self):
        aCo = self.xmlyUtil.getAlbumCount()
        self.assertIsInstance(aCo,type(0))

    def testGetAllCategoryWithCount(self):
        tmp = self.xmlyUtil.getAllCategoryWithCount()
        self.assertTrue(
            u'商业财经' in tmp
        )
        for i in tmp:
            print i , tmp[i]

    def testGetTotalAudioCount(self):
        tmp = self.xmlyUtil.getTotalAudioCount()
        print u'总共的audio 数目是 %d'%tmp
        self.assertIsNotNone(tmp)
        self.assertTrue(
            tmp<100000000
        )

    def testGetAllAudio(self):
        tmp = self.xmlyUtil.getAllAudio()
        tmp = tmp.next()
        self.assertIsNotNone(tmp)

    def testGetAllAlbumUrlWithCrawledAudiosId(self):
        audios = self.xmlyUtil.getAllAlbumUrlWithCrawledAudiosInfo()
        tmp = audios.next()
        self.assertTrue('href' in tmp)

    def testGetAlbumById(self):
        objectId = ObjectId("5710eacde13823643223484b")
        tmp = self.xmlyUtil.getAlbumById(objectId)
        self.assertEqual(tmp['album_name'],u"校园之声")

    def testGetAllAlbumByCategory(self):
        categoryName = u"【资讯】"
        albums = self.xmlyUtil.getAllAlbumByCategory(categoryName,1)
        self.assertEqual(
            albums.next()['categoryName'] ,u"【资讯】"
        )

    def testGetAudioAbloutCNR(self):
        audios = self.xmlyUtil.getAllAudioNotInCNR()
        audio = audios.next()
        self.assertIsNone(
            audio["sendToCNRTime"]
        )
        self.xmlyUtil.updateAudioSendTime(audio["_id"],datetime.datetime.now())
        audio = self.xmlyUtil.getAudioById(audio["_id"])
        self.assertIsNotNone(
            audio["sendToCNRTime"]
        )




#class TestCrawlManage(unittest.TestCase):
#    def testRandomDropAlbum(self):
#        crawlManage.randomDropAlbum(u'【娱乐】',100)

class TestQTUtil(unittest.TestCase):
    qtUtil = QTUtil()

    def testGetAlbumCount(self):
        count = self.qtUtil.getAlbumCount()
        self.assertIsNotNone(count)

    def testGetAudioCount(self):
        count = self.qtUtil.getTotalAudioCount()
        self.assertIsNotNone(count)

    def testGetCategoryWithCount(self):
        res = self.qtUtil.getAllCategoryWithCount()
        self.assertIn(u'\u519b\u4e8b',res)

class TestKLUtil(unittest.TestCase):
    klUtil = KLUtil()

    def testGetAlbumCount(self):
        tmp =  self.klUtil.getAlbumCount()
        print tmp

    def testGetAudioCount(self):
        tmp = self.klUtil.getTotalAudioCount()
        print tmp

    def testGetAllCategoryWithCount(self):
        tmp = self.klUtil.getAllCategoryWithCount()
        for key in tmp:
            print key,tmp[key]

    def testGetAudioAbloutCNR(self):
        audios = self.klUtil.getAllAudioNotInCNR()
        audio = audios.next()
        self.assertIsNone(
            audio["sendToCNRTime"]
        )
        self.klUtil.updateAudioSendTime(audio["_id"],datetime.datetime.now())
        audio = self.klUtil.getAudioById(audio["_id"])
        self.assertIsNotNone(
            audio["sendToCNRTime"]
        )


class TestCron(unittest.TestCase):
    def testGetRes(self):
        getSummary()

from m_interact.sender import Sender
from xml.etree.ElementTree import tostring
class TestSender(unittest.TestCase):
    '''
    测试 Sender 是否可以正常工作
    '''
    sender = Sender()
#   def testDictToXml(self):
#       testDict = {"wang":"xi"}
#       res = self.sender.dict_to_xml('root',testDict)
#       print tostring(res)
#       testDict = {"wang":{"xi":"yuan"}}
#       res = self.sender.dict_to_xml('root',testDict)
#       print tostring(res)
    def testUseJinja(self):
        self.sender.useJinja()

    def testGetXmlContent(self):
        xmly = db[ConfUtil.getXMLYAudioCollectionName()]
        kl = db[ConfUtil.getKLAudioCollectionName()]
        xmly_audio = xmly.find_one()
        kl_audio = kl.find_one()
        print self.sender.getXMLContent('kl',kl_audio)
        print self.sender.getXMLContent('xmly',xmly_audio)


if __name__ == "__main__":
    unittest.main()

