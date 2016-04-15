#coding=utf-8
'''
本模块仅仅为了在mongo 中定义一个统一的数据库格式
'''
__author__ = 'xiyuanbupt'

#比较严格的数据格式
class Structure:
    _fields = []
    def __init__(self,*args):
        if len(args) != len(self._fields):
            raise TypeError(
                'Expected {} arguments'.format(
                    len(self._fields)
                )
            )
        for name,value in zip(self._fields,args):
            setattr(self,name,value)
