#coding=utf-8
__author__ = 'xiyuanbupt'
# e-mail : xywbupt@gmail.com

import pymongo
import datetime


'''
本部分负责产生报表，即将某时刻产生的topn报表保存到mongo中
'''

mongo_uri = "mongodb://114.112.103.33:27017"
db_name = "test_spider"
client = pymongo.MongoClient(mongo_uri)

def write_qt_status(status):
    '''
    :param status:
    :return:
    '''
    print u'配置写死在代码中，如果为部署环境需要更改如下配置'

    db = client[db_name]

    # 保存status

    report = {'status':status}
    report['s_type'] = 'qt_full'
    report['time'] = datetime.datetime.now()
    db['qt_full_report'].insert(
        report
    )

