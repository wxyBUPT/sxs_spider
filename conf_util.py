#coding=utf-8
__author__ = 'xiyuanbupt'

class ConfUtil:

    @classmethod
    def getDBName(cls):
        return 'test_spider'

    @classmethod
    def getXMLYAlbumCollectionName(cls):
        return 'xmly_album'

    @classmethod
    def getXMLYCategoryCollectionName(cls):
        return 'xmly_category'

    @classmethod
    def getKLAlbumCollectionName(cls):
        return 'kl_album'

    @classmethod
    def getKLCategoryCollectionName(cls):
        return 'kl_category'

    @classmethod
    def getQTAlbumCollectionName(cls):
        return 'qt_item'

    @classmethod
    def getMongoIP(cls):
        return 'localhost'

    @classmethod
    def getMongoPort(cls):
        return 27017

    @classmethod
    def getCrontabDbCollectionName(cls):
        '''
        获得定期执行的脚本保存结果的 collection 名称
        :return:
        '''
        return 'crontab_result'

    @classmethod
    def getXMLYAudioCollectionName(cls):
        '''
        获得存储xmly 所有audio 信息的collection
        :return:
        '''
        return 'xmly_audio'

    @classmethod
    def getKLAudioCollectionName(cls):
        return 'kl_audio'

    @classmethod
    def getQTAudioCollectionName(cls):
        return 'qt_audio'

    @classmethod
    def getSoapTargetUri(cls):
        '''
        获得接收 从cnr 回调的地址
        :return:
        '''
        return "http://myhost:8080/toCNR/{sourceWeb}/{uuid}"

    @classmethod
    def getCrontabResultCollectionName(cls):
        return 'crontab_result'
