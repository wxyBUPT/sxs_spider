#coding=utf-8

import unittest

from m_interact.db import XMLYUtil,KLUtil,QTUtil

class TestXMLYUtil(unittest.TestCase):
    xmlyUtil = XMLYUtil()

    def testGetAlbumCount(self):
        count = self.xmlyUtil.getAlbumCount()
        self.assertIsInstance(count,type(0))

    def testGetAudioCount(self):
        count = self.xmlyUtil.getAuidoCount()
        self.assertIsNotNone(count)


class TestKLUtil(unittest.TestCase):
    klUtil = KLUtil()

    def testGetAlbumCount(self):
        count = self.klUtil.getAlbumCount()
        self.assertIsNotNone(count)

    def testGetAudioCount(self):
        count = self.klUtil.getAudioCount()
        self.assertIsNotNone(count)


class TestQTUtil(unittest.TestCase):
    qtUtil = QTUtil()

    def testGetAlbumCont(self):
        count = self.qtUtil.getAlbumCount()
        self.assertIsNotNone(count)

    def testGetAudioCount(self):
        count = self.qtUtil.getAudioCount()
        self.assertIsNotNone(count)

if __name__ == "__main__":
    unittest.main()