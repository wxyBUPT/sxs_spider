#coding=utf-8

__author__ = 'xiyuanbupt'
from dbTool.tool import XMLYUtil

from unittest import TestCase
import  unittest
from pprint import pprint
import json

from bson.objectid import ObjectId

import crawlManage
#http://www.ximalaya.com/16981310/album/374729
#被用于测试使用
class TestXMLYUtil(unittest.TestCase):
    xmlyUtil = XMLYUtil()

    def testGetAllAudioId(self):
        pass

    def testIsAudioInAlbum(self):
        self.assertTrue(
            self.xmlyUtil.isAudioInAlbum(
                "3249896","10199421"
            )
        )
        self.assertFalse(
            self.xmlyUtil.isAudioInAlbum(
                "3249896","11111111"
            )
        )

    def testGetAlbumCount(self):
        aCo = self.xmlyUtil.getAlbumCount()
        self.assertIsInstance(aCo,type(0))

    def testGetAllCategoryWithCount(self):
        tmp = self.xmlyUtil.getAllCategoryWithCount()
        self.assertTrue(
            u'【商业财经】' in tmp
        )
        for i in tmp:
            print i , tmp[i]

    def testGetTotalAudioCount(self):
        tmp = self.xmlyUtil.getTotalAudioCount()
        self.assertTrue(
            tmp>10000
        )
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
        objectId = ObjectId("56fcd397e1382347a544ba93")
        tmp = self.xmlyUtil.getAlbumById(objectId)
        self.assertEqual(tmp['album_name'],u"Кайрат Нуртас/hayrat nurtas/海拉提·努尔塔斯")

    def testGetAllAlbumByCategory(self):
        categoryName = u"【音乐】"
        albums = self.xmlyUtil.getAllAlbumByCategory(categoryName,1)
        self.assertEqual(
            albums.next()['categoryName'] ,u"【音乐】"
        )

#class TestCrawlManage(unittest.TestCase):
#    def testRandomDropAlbum(self):
#        crawlManage.randomDropAlbum(u'【娱乐】',100)



if __name__ == "__main__":
    unittest.main()

