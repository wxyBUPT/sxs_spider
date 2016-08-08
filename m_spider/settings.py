# -*- coding: utf-8 -*-

# Scrapy settings for m_spider project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#     http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
#     http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html
#日志配置
#为 root 添加一个Handler,logger

import logging
debug_log = logging.FileHandler(
        filename='./log/debug.log'
)
debug_log.setLevel(logging.WARNING)
logging.getLogger('').addHandler(debug_log)

SPIDER_MODULES = ['m_spider.spiders']
NEWSPIDER_MODULE = 'm_spider.spiders'
#设置splash 代理
#SPLASH_URL = 'http://192.168.99.100:8050'

#DOWNLOADER_MIDDLEWARES = {
#    'scrapyjs.SplashMiddleware': 725,
#}

#DUPEFILTER_CLASS = 'scrapyjs.SplashAwareDupeFilter'

#spider 与Django project结合，使用了Django 中的models
#做了如下更改

#import sys
#sys.path.append('/Users/xiyuanbupt/PycharmProjects/x_music/music_admin')
##print sys.path
#import os
#os.environ['DJANGO_SETTINGS_MODULE'] = 'music_admin.settings'
#import django
#django.setup()

#redis 设置
#内容分别为主机，端口，哪个数据库，密码
#REDIS_HOST = 'localhost'
#REDIS_PORT = 6379
#REDIS_DB = 0

#REDIS_PASS = None

#MongoDB 设置
MONGO_URI = 'mongodb://114.112.103.33:27017'
MONGO_DATABASE = 'test_spider'

#设置下载图片存储的位置
IMAGES_STORE = '/var/crawler/images'
FILES_STORE = '/var/crawler/audios'

XMLY_SETTINGS= {
        "IMAGES_STORE":'/var/crawler/xmly/images',
        "FILES_STORE":'/var/crawler/xmly/audios'
}
KL_SETTINGS = {
        "IMAGES_STORE":'/var/crawler/kl/images',
        "FILES_STORE":'/var/crawler/kl/audios'
}
QT_SETTINGS = {
        "IMAGES_STORE":'/var/crawler/qt/images',
        "FILES_STORE":'/var/crawler/qt/audios'
}
QINGTINGCONF = {
        'allowdomains' : ['qingting.fm'],
        'start_urls' : ['http://www.qingting.fm'],
        'playPR' : 'http://od.qingting.fm',
        'logfile' : 'qingting.log',
        'collection' : 'qingting_item',
        'qt_c_settings':{
        "IMAGES_STORE":'/var/crawler/qt/images',
        "FILES_STORE":'/var/crawler/qt/audios',
        }
}

# Crawl responsibly by identifying yourself (and your website) on the user-agent

#设置自定义限速

#USER_AGENT = 'm_spider (+http://www.yourdomain.com)'

# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS=32

# Configure a delay for requests for the same website (default: 0)
# See http://scrapy.readthedocs.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
#DOWNLOAD_DELAY=3
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN=16
#CONCURRENT_REQUESTS_PER_IP=16

# Disable cookies (enabled by default)
COOKIES_ENABLED=False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED=False

# Override the default request headers:
#DEFAULT_REQUEST_HEADERS = {
#   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#   'Accept-Language': 'en',
#}

# Enable or disable spider middlewares
# See http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'm_spider.middlewares.MyCustomSpiderMiddleware': 543,
#}
#SPIDER_MIDDLEWARES = {
#        'm_spider.middlewares.SaveInfoToDB':200,
#}

# Enable or disable downloader middlewares
# See http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
#DOWNLOADER_MIDDLEWARES = {
#    'm_spider.middlewares.MyCustomDownloaderMiddleware': 543,
#}

# Enable or disable extensioXmlyAudiosDownloader':747,
# See http://scrapy.readthedocs.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See http://scrapy.readthedocs.org/en/latest/topics/item-pipeline.html
#注意 itempipline 的优先级是 先过数字最小的，之后过数字对打的
ITEM_PIPELINES = {
#存储到 mongodb 中
        'm_spider.pipelines.SaveToMongo':800,
#        'm_spider.pipelines.KlimageDownloader':750,
#        'm_spider.pipelines.KlAudioDownloader':749,
#        'm_spider.pipelines.XmlyImageDownloader':748,
#        'm_spider.pipelines.XmlyAudiosDownloader':747,
}

# Enable and configure the AutoThrottle extension (disabled by default)
# See http://doc.scrapy.org/en/latest/topics/autothrottle.html
# NOTE: AutoThrottle will honour the standard settings for concurrency and delay
#设置限速
AUTOTHROTTLE_ENABLED=True
# The initial download delay
AUTOTHROTTLE_START_DELAY=5
# The maximum download delay to be set in case of high latencies
AUTOTHROTTLE_MAX_DELAY=60
# Enable showing throttling stats for every response received:
AUTOTHROTTLE_DEBUG=False

# Enable and configure HTTP caching (disabled by default)
# See http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED=True
#HTTPCACHE_EXPIRATION_SECS=0
#HTTPCACHE_DIR='httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES=[]
#HTTPCACHE_STORAGE='scrapy.extensions.httpcache.FilesystemCacheStorage'
#如下代码为设置随机用户代理
#USER_AGENT_LIST="/home/crawler/m_spider/m_spider/etc/user_agents.txt"
