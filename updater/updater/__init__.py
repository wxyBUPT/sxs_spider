#coding=utf-8

#将dbTool 添加到执行路径
import sys
from os import path
rootPath = path.abspath('./..')
if not rootPath in  sys.path:
    sys.path.append(rootPath)
