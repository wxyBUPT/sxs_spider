#coding=utf-8
#内容为定时脚本，定期执行获得数据库相关信息
__author__ = 'xiyuanbupt'

#将dbTool 添加到执行路径
import sys
from os import path
rootPath = path.abspath('./..')
if not rootPath in  sys.path:
    sys.path.append(rootPath)