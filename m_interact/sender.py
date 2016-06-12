#coding=utf-8
from __future__ import absolute_import
__author__ = 'xiyuanbupt'
import datetime
from xml.etree.ElementTree import Element
from jinja2 import Environment,PackageLoader
from pymongo import MongoClient
import requests

from conf_util import ConfUtil
env = Environment(loader=PackageLoader('m_interact','templates'))
'''
用于向接口中推送数据，每天会在固定的时间启动一个 sender 进程，用来推送当前的数据
'''
from m_spider.settings import XMLY_SETTINGS,KL_SETTINGS,QT_SETTINGS
client = MongoClient(ConfUtil.getMongoIP(),ConfUtil.getMongoPort())
db = client[ConfUtil.getDBName()]

from dbTool.tool import XMLYUtil,KLUtil,QTUtil

class Sender:
    klAudio = db[ConfUtil.getKLAudioCollectionName()]
    xmlyAudio = db[ConfUtil.getKLAudioCollectionName()]
    qtAudio = db[ConfUtil.getQTAudioCollectionName()]
    template = env.get_template('sendTemp.xml')
    soapTargetUri = ConfUtil.getSoapTargetUri()

    def __init__(self):
        self.xmlyUtil = XMLYUtil()
        self.qtUtil = QTUtil()
        self.klUtil = KLUtil()

    def useJinja(self):
        template = env.get_template('sendTemp.xml')
        return template.render(PGMGUID = 'wwww')

    #从数据库中读取所有未被推送到cnr 并且媒体文件已经被下载的数据项
    def getXMLYAudioNotInCNRWithFile(self):
        '''
        获得所有未被推送到CNR 但是媒体文件已经被下载的 audio
        '''
        cursor = self.xmlyAudio.find(
            {
                "sendToCNRTime":None,
                "audioDownloadDir":{"$ne":None}
            }
        )
        for audio in cursor:
            yield audio

    def getKLAudioNotInCNRWithFile(self):
        '''
        获得所有未被推送到CNR 但是媒体文件已经被下载的audio
        '''
        cursor = self.klAudio.find(
            {
                "sendToCNRTime":None,
                "audioDownloadDir":{"$ne":None}
            }
        )
        for audio in cursor:
            yield audio


    def getXMLContent(self,sourceWeb,audio):
        '''
        从audio 中获得 xml 内容
        函数会根据 sourceWeb 的不同来决定推送的逻辑
        sourceWeb 为 kl xmly 或者 qt
        '''
        now = datetime.datetime.now()
        RequestID = audio.get('uuid',None)
        RequestTime = now.strftime("%Y-%m-%d %H:%M:%S")
        TaskGUID = audio.get('uuid',None)
        TaskName = audio.get('album_title',None)
        PutinTime = now.strftime("%Y-%m-%d %H:%M:%S")
        uuid = audio.get('uuid',None)
        SoapTargetUri = self.soapTargetUri.format(
            sourceWeb = sourceWeb,uuid = uuid
        )
        PGMNAME = TaskName
        PGMGUID = audio.get('uuid',None)
        Title = TaskName
        #如下代码之后需要重构，已经将sourceWeb 写死在，故并不通用
        if sourceWeb == 'kl':
            CATALOGNAME = u'考拉fm\点播\{category}\{album}'.format(
                category = audio.get('categoryName',u'未知'),
                album = audio.get('albumName',u'未知')
            )
            CreatorName = audio.get('uploaderName',u'北邮爬虫')
            PgmNote = audio.get('fullDescs',u'描述未知')
            FileName = audio.get('audioDownloadDir',None)
        elif sourceWeb == 'xmly':
            CATALOGNAME = u'喜马拉雅fm\点播\{category}\{album}'.format(
                category = audio.get('category_title',u'未知'),
                album = audio.get('album_title',u'未知')
            )
            CreatorName = audio.get('uploadUserName',u'北邮爬虫')
            PgmNote = audio.get('intro',u'描述未知')
            FileName = audio.get('audioDownloadDir',None)
        else:
            print u'未知sourceWeb'
        xmlContent = self.template.render(
            RequestID = RequestID,
            RequestTime = RequestTime,
            TaskGUID = TaskGUID,
            PutinTime = PutinTime,
            uuid = uuid,
            SoapTargetUri = SoapTargetUri,
            PGMNAME = PGMNAME,
            PGMGUID = PGMGUID,
            Title = Title,
            CATALOGNAME = CATALOGNAME,
            CreatorName = CreatorName,
            PgmNote = PgmNote,
            FileName = FileName,
            TaskName = TaskName,
            firstplaytime = None,
            broadstarttime = None,
            broadendtime = None
        )

        return xmlContent

    def getAudioPutToCNR(self):
        '''
        执行获得所有未被推送到cnr ，并且文件已经被下载到本地种的audio 并将其推送至cnr
        并更改标志位
        '''
        pass







#   def dict_to_xml(self,tag,d):
#       '''
#       Trun a simple dict of key/value pairs into XML
#       :param tag:
#       :param d:
#       :return:
#       '''
#       elem = Element(tag)
#       for key,val in d.items():
#           if type(val) == type({}):
#               elem.append(self.dict_to_xml(key,val))
#           else:
#               child = Element(key)
#               child.text = str(val)
#               elem.append(child)
#       return elem


