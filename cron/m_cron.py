#coding=utf-8
__author__ = 'xiyuanbupt'
from dbTool.tool import XMLYUtil,KLUtil,QTUtil,db
from conf_util import ConfUtil

#每一个执行，获得获得当前有的专辑数目，歌曲数目

def getSummary():
    '''
    获得当前数据库状态的整体描述
    :return:
    '''
    xmlyUtil = XMLYUtil()
    klUtil = KLUtil()
    qtUtil = QTUtil()

    qtRes = {}
    klRes = {}
    xmlyRes = {}
    qtRes['albumCount'] = qtUtil.getAlbumCount()
    qtRes['audioCount'] = qtUtil.getTotalAudioCount()
    qtRes['categoryWithCount'] = qtUtil.getAllCategoryWithCount()
    xmlyRes['albumCount'] = xmlyUtil.getAlbumCount()
    xmlyRes['audioCount'] = xmlyUtil.getTotalAudioCount()
    xmlyRes['categoryWithCount'] = xmlyUtil.getAllCategoryWithCount()
    klRes['albumCount'] = klUtil.getAlbumCount()
    klRes['audioCount'] = klUtil.getTotalAudioCount()
    klRes['categoryWithCount'] = klUtil.getAllCategoryWithCount()
    res = dict(
        totalAlbumCount = qtRes['albumCount'] + xmlyRes['albumCount'] + klRes['albumCount'],
        totalAudioCount = qtRes['audioCount'] + qtRes['audioCount'] + klRes['audioCount'],
        qtRes = qtRes,
        klRes = klRes,
        xmlyRes = xmlyRes,
        type = 'summary'
    )
    db[ConfUtil.getCrontabDbCollectionName()].insert(res)

#统计点播节目期数
