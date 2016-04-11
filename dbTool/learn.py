#coding=utf-8
__author__ = 'xiyuanbupt'
class Foo:
    def __new__(cls, *args, **kwargs):
        print "new called"
        return object.__new__()

    def __init__(self):
        print 'init called'

    def foo(self):
        print 'foo called'

foo = Foo()
bar = Foo()
z = Foo()
