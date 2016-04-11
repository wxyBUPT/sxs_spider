#!/usr/bin/python
#coding=utf=8
from __future__ import absolute_import
import argparse
'''
命令行参数管理，许多操作多在这里完成
'''
__author__ = 'xiyuanbupt'
from dbTool.tool import XMLYUtil

def randomDropAlbum(categoryName,dropCount):
    '''
    因硬盘空间不够用，随机删除一些数据
    :param categoryName:
    :param dropCount:
    :return:
    '''
    xmlyUtil = XMLYUtil()
    audios = xmlyUtil.getAllAlbumByCategory(categoryName,dropCount)
    for audio in audios:
        _id = audio['_id']
        xmlyUtil.deleteAlbumWithFiles(_id)



def parse():
    #创建一个解析器
    parser = argparse.ArgumentParser(
        description = u'爬虫命令行管理工具'
    )
    #添加参数，通过add_argument() 方法向 ArgumentParser 添加程序参数的信息
    #这些信息将告诉 ArgumentParser 如何接受命令上的字符串并将它们转换成
    #对象。这些信息被保存下来并在调用parse_args() 的时候用到
    # add_argument() 方法中各个参数的含义
    # name or flags 想想字符串或者列表，例如 foo 或者 -f --foo
    # action 在命令行遇到该参数时候采取基本的动作类型
    # nargs 应该读取的命令行参数的数目
    # const 某些action 和nargs 选项要求的常数值
    # default 如果命令行中没有出现该参数时的默认值
    # type 命令行参数应该被转换成的类型
    # choices 参数课允许的值的一个容器
    # required 该命令行选项是否可以被忽略，（）只针对可选参数
    # help 参数的剪短描述
    # metavar 参数在帮助信息中显示的名字
    # dest 给parse_args() 返回的对象要添加的属性名称
    # 可选的参数可以使用  --f --foo 中使用
    # 而为之参数

    #nargs 参数描述的是

    #添加version 参数
    parser.add_argument(
        '-v','--version',action = 'version',version = '%(prog)s 0.1'
    )
    parser.add_argument(
        'integers',metavar = 'N',type = int,nargs = '+',
        help = 'an integer for the accumulator'
    )
    parser.add_argument(
        '--i',type = int,nargs = '+',
        help = u'我就是试试程序是否可以正常执行'
    )
    parser.add_argument(
        '--sum' , dest = 'accumulate',action = 'store_const',
        const = sum , default= max,
        help = 'sum the integers (default:find the max)'
    )
    args = parser.parse_args()
    print args.accumulate(args.integers)
    print vars(args)

if __name__ == "__main__":
    parse()