# -*- coding: utf-8 -*-
from __future__ import absolute_import
import json
import logging,datetime

import scrapy,requests

from crawl_util import get_js_timestamp
from ..items import KLCotagoryMetaItem,KLAudio,KLAlbum,KLCategory,KLAlbumMetaItem

logging.basicConfig(
    filename = 'crawl.log',
    format = "%(levelname) -10s %(asctime)s %(module)s:%(lineno)s %(funcName)s %(message)s",
    level = logging.ERROR
)

#http://www.kaolafm.com/webapi/resource/search?cid=1&rt
# ype=20000&sorttype=HOT_RANK_DESC&pagesize=24&pagenum=2&_=1458178696146
#ef get_start_urls():
#   '''
#   通过Django数据库获得开始爬取的url
#   :return:
#   '''
#   klMetas = KLMeta.objects.all()
#   for klMeta in klMetas:
#       page_count = klMeta.max_pagenum
#       cid = klMeta.cid
#       pagesize = klMeta.pagesize
#       tag = klMeta.tag
#       for i in range(1,page_count+1):
#           params = urllib.urlencode(
#               {
#                   'cid':cid,
#                   'rtype':20000,
#                   'sorttype':'HOT_RANK_DESC',
#                   'pagesize':pagesize,
#                   'pagenum':i,
#                   '_':get_js_timestamp(),
#               }
#           )
#           url = 'http://www.kaolafm.com/webapi/resource/search?%s'%(params)
#           yield url

#class KaolafmSpider(scrapy.Spider):
#    name = "kaolafm"
#    allowed_domains = ["kaolafm.com"]
    #start_urls = (
    #    #'http://www.kaolafm.com/zj/rsrTIWQd.html',
    #    server_time = 1458175503575,
    #    'http://www.kaolafm.com/webapi/resource/search?cid=727&rtype=20000&sorttype=HOT_RANK_DESC&pagesize=24&pagenum=2&_=1458175543964',
    #    'http://www.kaolafm.com/webapi/resource/search?cid=727&rtype=20000&sorttype=HOT_RANK_DESC&pagesize=24&pagenum=1&_=1458175503007',
    #    'http://www.kaolafm.com/webapi/category/list?fid=727&_=1458175503204',
    #    'http://www.kaolafm.com/webapi/category/list?fid=0&_=1458175503417',
    #    'http://www.kaolafm.com/webapi/resource/search?cid=727&rtype=20000&sorttype=HOT_RANK_DESC&pagesize=24&pagenum=2&_=1458175543964',
    #)
#    start_urls = get_start_urls()
#    def start_requests(self):
#        for url in self.start_urls:
#            yield scrapy.Request(
#                url,self.parse,
#            )
#
#
#    def parse(self, response):
#        from scrapy.shell import inspect_response
#        inspect_response(response,self)
#        pass

#重构上面的代码
class KaolafmSpider(scrapy.Spider):

    name = "kaolafm"
    allowed_domains = ["kaolafm.com"]

    #维护一个有效的 category 名称的列表，如果不在列表中，则相应的地址不跟进
    effectiveCategorys = (
        u"大牌节目",u'名人专辑',u'情感',u'搞笑',u'小说',
        u'新闻',u'音乐',u'脱口秀',u'相声评书',u'两性',u'吐槽机',
        u'综艺娱乐',u'广播剧',u'讲座讲坛',u'亲子',u'外语',
        u'星座风水',u'恐怖故事',u'科技',u'汽车',u'财经',u'社科历史',
        u'生活',u'体育',u'健康',u'教育',u'军事',u'动漫游戏',u'校园',
        u'电视影音',u'宗教信仰',u'公益'
    )

    headers = {
        "Host":"www.kaolafm.com",
        "User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10.11; rv:44.0) Gecko/20100101 Firefox/44.0",
        "Accept":"application/json, text/javascript, */*; q=0.01",
        "Referer":"zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3",
    }

    #获得javascript 的时间戳
    js_timestamp = get_js_timestamp()

    start_urls = [
            "http://www.kaolafm.com/webapi/category/list?fid=0&_=%d"%(js_timestamp),
    ]
    def parse(self, response):
        json_str_body = response.body
        json_dict_body = json.loads(json_str_body)
        self.logger.info(
            u'获得初始地址数据，%s code为 %s'%(response.url,json_dict_body['code'])
        )
        try:
            if json_dict_body['message'] != "success":
                raise Exception(u'获得初始地址失败，尝试重新获取')
        except Exception as et:
            self.logger.critical(u'%s'%(et.args))
            return

        #如下代码为获得 category 对应的id，category 的logo，以及categry 的地址
        dataList = json_dict_body['result']['dataList']
        for data in dataList:
            if data['categoryName'] not in self.effectiveCategorys:
                continue

            item = KLCotagoryMetaItem()
            item['categoryId'] = data.get('categoryId',None)
            item['categoryName'] = data.get('categoryName',None)
            item['hasSub'] = data.get('hasSub',None)
            item['logoUrl'] = data.get('logo',None)
            item['imageAoyo'] = data.get('imageAoyo',None)
            item['imageAoyoEffect'] = data.get('imageAoyoEffect',None)

            js_timestamp = get_js_timestamp()
            categoryUrl = 'http://www.kaolafm.com/webapi/resource/search?cid=%d&rtype=20000&sorttype=HOT_RANK_DESC&pagesize=24&pagenum=1&_=%d'%(item['categoryId'],js_timestamp)
            meta = {
                #禁掉 cookie
                'dont_merge_cookies':True,
                'item':item
            }
            request = scrapy.Request(
                categoryUrl,
                callback=self.parse_category,
                headers=self.headers,
                meta = meta
            )
            #request.meta = meta
            yield request

    def parse_category(self,response):
        '''
        用于处理所有的category ，负责 yield categoryItem ，
        同时负责yield 带有meta 的 album request
        :param response:
        :return:
        '''
        item = response.meta['item']

        #下面内容负责yield category 相应的item
        klC = KLCategory()
        klC['categoryId'] = item['categoryId']
        klC['categoryName'] = item['categoryName']
        klC['sourceUrl'] = 'http://www.kaolafm.com/category/%s'%(klC['categoryId'])

        #下面内容为通过 response 获得
        json_str_body = response.body
        dict_body = json.loads(json_str_body)
        try:
            if dict_body['message'] != u'success':
                raise Exception(
                    u"接口数据获取错误%s"%(response.url)
                )
        except Exception as et:
            self.logger.error(et.args)
        res = dict_body['result']
        klC['totalPages'] = res.get('totalPages',None)
        klC['totalCounts'] = res.get('totalCounts',None)
        klC['pageSize'] = res.get('pageSize',None)

        #通过接口 http://www.kaolafm.com/webapi/category/list?fid=727&_=1458611930057
        #获得子类别的信息
        js_timestamp = get_js_timestamp()
        getSubCategoryUrl = 'http://www.kaolafm.com/webapi/category/list?fid=%s&_=%d'%(
            klC['categoryId'],js_timestamp
        )

        subCResDict = requests.get(getSubCategoryUrl).json()
        try:
            if subCResDict['message'] != u'success':
                raise Exception(
                    u'未能获得子类别信息，请求地址 %s'%(getSubCategoryUrl)
                )
        except Exception as et:
            self.logger.error(et.args)
        subCategorys = subCResDict['result']['dataList']
        #子类别的音频文件，以及logo 信息在pipline 中获得
        klC['subCategorys'] = subCategorys
        #yield 出的内容由 pipline 处理，在本处不用处理
        yield klC

        #catogry 内容已经处理完毕，下面内容负责处理处理相应的 album
        #接口的开始信息有如下接口获得
        # http://www.kaolafm.com/webapi/resource/search?cid=727&rtype=20000&sorttype=HOT_RANK_DESC&pagesize=24&pagenum=1&_=1458611929745
        #如下内容可以重构为一个函数，但是目前考虑如果重构为函数需要传递的参数太多，故直接以代码的形式
        cid = int(item['categoryId'])
        totalPages = int(klC['totalPages'])
        pageSize = int(klC['pageSize'])
        categoryName = klC['categoryName']
        #处理完category 的信息开始处理album 相关的信息
        #目前获取的信息为根据热度排序获得的
        #本次循环得到了对应类别下的所有ablum的初始化信息
        for page in range(1,totalPages+1):
            js_timestamp = get_js_timestamp()
            tmpUrl = 'http://www.kaolafm.com/webapi/resource/search?cid=%d&rtype=20000&sorttype=HOT_RANK_DESC&pagesize=%d&pagenum=%d&_=%s'%(
                cid,pageSize,page,js_timestamp
            )
            tmpRes = requests.get(tmpUrl,headers = self.headers)
            resDict = tmpRes.json()
            try:
                if resDict['message']  != u'success':
                    raise Exception(
                        u"can't get ：%s，page %s  album info, pageConteng:%s"%(
                            cid,page,resDict
                        )
                    )
            except Exception as et:
                self.logger.error(et.args)
            dataList = resDict['result']['dataList']
            #对每一个album 执行如下获得操作
            for index,data in enumerate(dataList):
                item = KLAlbumMetaItem()
                item['categoryId'] = cid
                item['categoryName'] = categoryName
                item['categoryPage'] = page
                item['index'] = index

                item['albumId'] = data.get('id',None)
                item['type'] = data.get('type',None)
                item['comeFrom'] = data.get('comeFrom',None)
                item['comeFromId'] = data.get('comeFromId',None)
                item['albumPicUrl'] = data.get('pic',None)
                item['followedNum'] = data.get('followedNum',None)
                item['listenNum'] = data.get('listenNum',None)
                item['shortDesc'] = data.get('desc',None)
                item['albumName'] = data.get('albumName',None)
                #type(tmp) is list
                item['anchors'] = data.get('host',None)
                meta = {
                    #禁掉cookie
                    'dont-merge_cookies':True,
                    'item':item
                }
                #如下步骤需要计算对应的url 信息，因为使用nodejs 计算，故需要启动额外的进程
                #通过如下接口获得信息 http://www.kaolafm.com/webapi/albumdetail/get?albumid=1100000000343&_=1458633786987
                cur_js_timestamps = get_js_timestamp()
                albumDetailUrl = 'http://www.kaolafm.com/webapi/albumdetail/get?albumid=%s&_=%s'%(
                    item['albumId'],cur_js_timestamps
                )
                request = scrapy.Request(
                    url = albumDetailUrl,
                    callback = self.parse_album,
                    headers = self.headers,
                    meta = meta
                )
                yield request


    def parse_album(self,response):
        item = response.meta['item']
        cid = item['categoryId']
        klAlbum = KLAlbum()
        klAlbum.update(item)
        klAlbum['lastModifyTime'] = datetime.datetime.now()

        #通过返回的 body 值获得信息
        bodyD = json.loads(response.body)

        try:
            if bodyD['message'] != u'success':
                raise Exception(u'get url:  content fail'%(
                    response.url
                ))
        except Exception as et:
            self.logger.error(et.args)
        result = bodyD.get('result',None)
        #如下内容为 unicode形式的数组

        klAlbum['tags'] = result.get('keyWords',None)
        klAlbum['fullDescs'] = result.get('radioDesc',None)
        klAlbum['audioCounts'] = result.get('countNum',None)
        klAlbum['shareUrl'] = result.get('shareUrl',None)
        klAlbum['produce'] = result.get('produce',None)
        klAlbum['status'] = result.get('status',None)
        klAlbum['updateDay'] = result.get('updateDay',None)
        klAlbum['uploadUserName'] = result.get('uploadUserName',None)
        klAlbum['commentCount'] = result.get('commentNum',None)
        klAlbum['uploaderId'] = result.get('uploaderId',None)

        #如下内容为通过一系列接口 http://www.kaolafm.com/webapi/audios/list?id=1100000000343&pagesize=20&pagenum=1&sorttype=1&_=1458638856724
        #获得数据
        #如下代码获得当前的album 有多少歌曲
        js_timstamp = get_js_timestamp()
        id = klAlbum['albumId']
        getAudiosUrl = 'http://www.kaolafm.com/webapi/audios/list?id=%s&pagesize=20&pagenum=1&sorttype=1&_=%s'%(
            id,js_timstamp
        )
        fAudiosDict = requests.get(getAudiosUrl,headers = self.headers).json()
        result = fAudiosDict['result']
        sumPage = int(result.get('sumPage',None))
        klAlbum['sumPage'] = sumPage
        klAlbum['pageSize'] = result.get('pageSize',None)
        audioList = []

        #如下步骤对album 中的每一页的歌曲做处理
        for i in range(1,sumPage+1):
            js_timstamp = get_js_timestamp()
            getAudiosUrl = 'http://www.kaolafm.com/webapi/audios/list?id=%s&pagesize=20&pagenum=%d&sorttype=1&_=%s'%(
                id,i,js_timstamp
            )
            audiosDict = requests.get(getAudiosUrl,headers = self.headers).json()
            try:
                if audiosDict['message'] != u'success':
                    raise Exception(u'get audio list fail , url is %s'%(
                        getAudiosUrl
                    ))
            except Exception as et:
                self.logger.error(et.args)

            result = audiosDict.get('result',None)
            dataList = result.get('dataList',None)
            #如下步骤获得某一页中的所有audio 信息
            for data in dataList:
                klAudio = KLAudio()
                klAudio['audioId'] = data.get('audioId',None)
                klAudio['audioName'] = data.get('audioName',None)
                klAudio['audioPicUrl'] = data.get('aduioPic',None)
                klAudio['audioDesc'] = data.get('audioDesc',None)
                #在电台中对应的期数，非常重要的一个信息
                klAudio['orderNum'] = data.get('orderNum',None)
                klAudio['playUrl'] = data.get('playUrl',None)
                klAudio['mp3PlayUrl'] = data.get('mp3PlayUrl',None)
                klAudio['accPlayUrl'] = data.get('accPlayUrl',None)
                klAudio['m3u8PlayUrl'] = data.get('m3u8PlayUrl',None)
                klAudio['shareUrl'] = data.get('shareUrl',None)
                klAudio['fileSize'] = data.get('fileSize',None)
                klAudio['updateTime'] = data.get('updateTime',None)
                klAudio['createTime'] = data.get('createTime',None)
                klAudio['duration'] = data.get('duration',None)
                klAudio['listenNum'] = data.get('listenNum',None)
                klAudio['likedNum'] = data.get('likedNum',None)
                klAudio['commentNum'] = data.get('commentNum',None)
                klAudio['uploaderId'] = data.get('uploaderId',None)
                klAudio['uploaderName'] = data.get('uploaderName',None)
                audioList.append(klAudio)
        #将数据加载到 klAlbum
        klAlbum['audios'] = audioList

        yield  klAlbum