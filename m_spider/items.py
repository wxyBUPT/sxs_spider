# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


#重构的代码，上面代码基本不再使用，定义Items
class KLCategory(scrapy.Item):
    '''
    考拉fm 下面每一类的点播内容
    '''
    collection = "kl_category"
    #来源网站
    contentSource = "www.kaolafm.com"
    #新添加一个冗余字段，本字段可能不被使用
    s_type = "kl_category"

    #以下内容为 “树根” 通过网页爬取获得。
    #如下字段特别重要，并需要设置unique = true
    categoryId = scrapy.Field()
    #类别名称
    categoryName = scrapy.Field()
    #类别的url 地址
    sourceUrl = scrapy.Field()
    #子类别内容，为set 的形式
    subCategorys = scrapy.Field()

    #以下内容为通过接口  http://www.kaolafm.com/webapi/resource/search?cid=699&rtype=20000&sorttype=HOT_RANK_DESC&pagesize=24&pagenum=1&_=1458565508359
    #获得，
    #总共的页数
    totalPages = scrapy.Field()
    #类别内容总共的电台数目
    totalCounts = scrapy.Field()
    #每一页中专辑的数目
    pageSize = scrapy.Field()



#类别只用电台的名称来记录
class KLAlbum(scrapy.Item):
    '''
    考拉下面每一电台的内容数据
    '''
    #Category 类别，相当于 mysql 中的foreigh key
    collection = 'kl_album'
    contentSource = 'www.kaolafm.com'
    s_type = 'kl_album'

    #下面页面为从 category 中获得
    #对应类别的id，需要在数据库中为id 建立索引
    categoryId = scrapy.Field()
    #所属的类别名称，为一个集合的形式保存，之所以以集合的形式表示，是因为有可能一个album 可能属于不同的类别
    categoryName = scrapy.Field()
    #在相应类别中的第几页
    categoryPage = scrapy.Field()
    #在对应页数中的第几行的数据
    index = scrapy.Field()

    #如下内容通过http://www.kaolafm.com/webapi/resource/search?cid=699&rtype=20000&sorttype=HOT_RANK_DESC&pagesize=24&pagenum=1&_=1458565508359 接口返回的数据获得
    #对应电台的id，添加索引，并且unique = true
    albumId = scrapy.Field()
    #对应的type，返回值中的内容，具体形式是什么我也不知道
    type = scrapy.Field()
    #如下两个字段都是返回内容就有的，也不知道具体的含义是什么
    #电台的来源
    comeFrom = scrapy.Field()
    #电台来源的id
    comeFromId = scrapy.Field()
    #电台的图片对应的url
    albumPicUrl = scrapy.Field()
    #电台的关注人数
    followedNum = scrapy.Field()
    #电台被收听的次数
    listenNum = scrapy.Field()
    #电台的简单描述
    shortDesc = scrapy.Field()
    #电台名称
    albumName = scrapy.Field()
    #主播，一个电台可能有很多的主播
    anchors = scrapy.Field()

    #下面这个字段为数据爬取的时候添加上的字段
    #最后更新的时间
    lastModifyTime = scrapy.Field()

    #如下的字段内容都是通过访问相关album 的地址得到的，例如 http://www.kaolafm.com/zj/dU28U_zG.html
    #有些内容可以在之前的请求中获得，故忽略掉
    #推荐的理由，为标题下面的一行字
    #likeReason = scrapy.Field()
    #标签,定义为一个集合的形式
    tags = scrapy.Field()
    #全部的描述，内容为数组的形式
    fullDescs = scrapy.Field()

    #下面内容为通过接口  http://www.kaolafm.com/webapi/audios/list?id=1100000048214&pagesize=20&pagenum=7&sorttype=1&_=1458566493747 获得
    #专辑内总共的歌曲数目
    audioCounts = scrapy.Field()
    #分享连接
    shareUrl = scrapy.Field()
    #来源
    produce = scrapy.Field()
    #状态，例如更新中
    status = scrapy.Field()
    #更新时间
    updateDay = scrapy.Field()
    #上传者name
    uploadUserName = scrapy.Field()
    #评论数目
    commentCount = scrapy.Field()
    #上传者id
    uploaderId = scrapy.Field()


    #专辑中总共的页数
    sumPage = scrapy.Field()
    #专辑中一页的audio 数目
    pageSize = scrapy.Field()
    #本内容为音频相关信息组成的列表内容
    #列表中的元素为 audio 实例
    #audios = [klaudio[1],klaudio[2]]
    audios = scrapy.Field()

    #如下内容为 audio 所有的图片存储位置
    albumPics = scrapy.Field()
    albumSounds = scrapy.Field()



    #接下来的内容为歌曲相关的内容，


class KLAudio(scrapy.Item):
    '''
    对应kaola fm 中的音频内容
    '''
    s_type = 'kl_audio'
    collection = 'kl_audio'
    #歌曲id
    audioId = scrapy.Field()
    #歌曲的url 地址，大多数时候获得不到电台的url 地址,当前被注释掉
    #audioUrl = scrapy.Field()
    #歌曲的名称
    audioName = scrapy.Field()
    #歌曲图片的url
    audioPicUrl = scrapy.Field()
    #歌曲图片本地地址，或者存在mongodb 中，此内容会与 电台的图片有重复，故需要设置一套机制，避免重复的下载
    #将当前信息注释掉，在pipline 中获得
    #audioPicLocalPath = scrapy.Field()
    #歌曲的简单描述
    audioDesc = scrapy.Field()
    #歌曲在电台中对应的期数
    orderNum = scrapy.Field()
    #播放地址
    playUrl = scrapy.Field()
    #mp3 播放的地址
    mp3PlayUrl = scrapy.Field()
    #acc 播放的地址
    accPlayUrl = scrapy.Field()
    #页面中的m3u8PlayUrl
    m3u8PlayUrl = scrapy.Field()
    #shareUrl
    shareUrl = scrapy.Field()
    #请求中返回的fileSize
    fileSize = scrapy.Field()
    #非常重要的一个字段，更新的时间，为歌曲在相应网站上发布的时间
    updateTime = scrapy.Field()
    #创建时间，一般情况下和updateTime 相近，但是为时间戳的形式
    createTime = scrapy.Field()
    #持续时间，duration
    duration = scrapy.Field()
    #被收听的次数
    listenNum = scrapy.Field()
    #被标注为喜欢的次数
    likedNum = scrapy.Field()
    #评论数
    commentNum = scrapy.Field()
    uploaderName = scrapy.Field()
    uploaderId = scrapy.Field()
    album_title = scrapy.Field()
    category_title = scrapy.Field()

    #用于保存categoryName
    categoryName = scrapy.Field()
    albumName = scrapy.Field()
    fullDescs = scrapy.Field()


'''
{u'aacPlayUrl': u'http://image.kaolafm.net/mz/aac_/201602/663f4aa1-d01b-4c3b-9d99-076c2b50264e.aac',
   u'albumId': 1100000000343,
   u'albumName': u'\u8001\u6881\u6545\u4e8b\u6c47',
   u'albumPic': u'http://image.kaolafm.net/mz/images/201409/4fd9fe60-2d20-4068-9bc2-b2546a7307fc/default.jpg',
   u'audioDes': u'\u201c\u6253\u9171\u6cb9\u201d\u7684\u9547\u5143\u5927\u4ed9',
   u'audioId': 1000002264731,
   u'audioName': u'\u201c\u6253\u9171\u6cb9\u201d\u7684\u9547\u5143\u5927\u4ed9',
   u'audioPic': u'http://image.kaolafm.net/mz/images/201409/4fd9fe60-2d20-4068-9bc2-b2546a7307fc/default.jpg',
   u'categoryId': 143,
   u'clockId': u'',
   u'commentNum': 14,
   u'createTime': 1456317750000,
   u'duration': 1393516,
   u'fileSize': 11108012,
   u'hasCopyright': 1,
   u'host': [],
   u'isStored': 0,
   u'islistened': 0,
   u'likedNum': 17,
   u'listenNum': 22035,
   u'm3u8PlayUrl': u'http://image.kaolafm.net/mz/aac_/201602/663f4aa1-d01b-4c3b-9d99-076c2b50264e/playlist.m3u8',
   u'mp3PlayUrl': u'http://image.kaolafm.net/mz/audios/201602/663f4aa1-d01b-4c3b-9d99-076c2b50264e.mp3',
   u'orderNum': 550,
   u'playUrl': u'http://image.kaolafm.net/mz/outopus_16/201602/663f4aa1-d01b-4c3b-9d99-076c2b50264e.opus',
   u'shareUrl': u'http://m.kaolafm.com/share/jm.html?audioId=1000002264731',
   u'tips': u'',
   u'type': 1,
   u'updateTime': u'2016-02-24',
   u'uploaderId': 2091609,
   u'uploaderName': u'\u542c\u597d\u518d\u6765'}
'''

#为获得完整的kl_category 信息新添加的 item，不用于储存，只用于
#在爬虫之间的相互步骤沟通数据
class KLCotagoryMetaItem(scrapy.Item):
    categoryId = scrapy.Field()
    categoryName = scrapy.Field()
    #是否有子标签
    hasSub = scrapy.Field()
    #logo 的url 位置
    logoUrl = scrapy.Field()
    #下面两项 前端页面就是这么定义的，我也不知道是什么
    imageAoyo = scrapy.Field()
    imageAoyoEffect = scrapy.Field()

#如下内容为从接口 http://www.kaolafm.com/webapi/resource/search?cid=727&rtype=20000&sorttype=HOT_RANK_DESC&pagesize=24&pagenum=1&_=1458611929745
#获得数据的 meta 信息，将会被添加到 request 的meta 中，不用于存储，只用于爬虫之间的数据交换

class KLAlbumMetaItem(scrapy.Item):
    #下面页面为从 category 中获得
    #对应类别的id，需要在数据库中为id 建立索引
    categoryId = scrapy.Field()
    #所属的类别名称，为一个集合的形式保存，之所以以集合的形式表示，是因为有可能一个album 可能属于不同的类别
    categoryName = scrapy.Field()
    #在相应类别中的第几页
    categoryPage = scrapy.Field()
    #在对应页数中的第几行的数据
    index = scrapy.Field()

    #如下内容通过http://www.kaolafm.com/webapi/resource/search?cid=699&rtype=20000&sorttype=HOT_RANK_DESC&pagesize=24&pagenum=1&_=1458565508359 接口返回的数据获得
    #对应电台的id，添加索引，并且unique = true
    albumId = scrapy.Field()
    #对应的type，返回值中的内容，具体形式是什么我也不知道
    type = scrapy.Field()
    #如下两个字段都是返回内容就有的，也不知道具体的含义是什么
    #电台的来源
    comeFrom = scrapy.Field()
    #电台来源的id
    comeFromId = scrapy.Field()
    #电台的图片对应的url
    albumPicUrl = scrapy.Field()
    #电台的关注人数
    followedNum = scrapy.Field()
    #电台被收听的次数
    listenNum = scrapy.Field()
    #电台的简单描述
    shortDesc = scrapy.Field()
    #电台名称
    albumName = scrapy.Field()
    #主播,注意，一个电台可能有很多的主播
    anchors = scrapy.Field()

class XMLYCategory(scrapy.Item):
    '''
    喜马拉雅fm 的点播分类内容
    '''
    collection = "xmly_category"
    contentSource = 'www.ximalaya.com'
    s_type = "xmly_category"

    #网站类别的cid
    cid = scrapy.Field()
    #类别对应的英文名称
    cname = scrapy.Field()
    #类别对应的url 地址
    href = scrapy.Field()
    #类别下面对应得子类别
    subCategorys = scrapy.Field()
    #对应中文名称
    nameText = scrapy.Field()


class XMLYAlbum(scrapy.Item):
    '''
    喜马拉雅fm 对应的专辑信息
    '''
    collection = 'xmly_album'
    contentSource = 'www.ximalaya.com'
    s_type = 'xmly_album'

    categoryName = scrapy.Field()


    #上传主播的信息
    uploadUserName = scrapy.Field()
    #上传主播的主页
    uploadUserUrl = scrapy.Field()

    #album 原始的url地址
    href = scrapy.Field()

    album_id = scrapy.Field()

    album_name = scrapy.Field()
    #对应的标签
    tags = scrapy.Field()

    #播放的次数，可能在原来网站中是 以万为单位的，需要变为 integer
    playTime = scrapy.Field()

    #网站图片的 url 连接
    imgSrc = scrapy.Field()
    #专辑的描述信息，有的专辑可能没有相关的描述信息
    albumDesc = scrapy.Field()
    #下面的字段为数据爬取的时候添加上去的字段
    #对应专辑里面的 audio
    audios = scrapy.Field()
    #专辑里面audios 的个数
    audiosCount = scrapy.Field()

    audiosImages = scrapy.Field()
    audiosFiles = scrapy.Field()

#如下内容为两个爬取之间用于信息传递的中间状态
class XMLYAlbumMeta(scrapy.Item):

    href = scrapy.Field()
    album_id = scrapy.Field()
    imgSrc = scrapy.Field()
    album_name = scrapy.Field()
    playTime = scrapy.Field()


class XMLYAudio(scrapy.Item):
    '''
    对应喜马拉雅fm 中的音频内容，目的是规定音频中都有哪些字段
    前半部分的内容通过接口 http://www.ximalaya.com/tracks/13569779.json
    获得
    中间部分内容通过地址
    http://www.ximalaya.com/36327519/sound/11362725
    获得
    '''
    collection = 'xmly_audio'
    contentSource = 'www.ximalaya.com'
    s_type = 'xmly_audio'

    #歌曲的id
    id = scrapy.Field()
    #歌曲文件地址的三个连接
    play_path_64 = scrapy.Field()
    play_path_32 = scrapy.Field()
    play_path = scrapy.Field()

    duration = scrapy.Field()
    title = scrapy.Field()
    nickname = scrapy.Field()
    uid = scrapy.Field()
    upload_id = scrapy.Field()

    #歌曲的封面的图片连接地址
    cover_url = scrapy.Field()
    cover_url_142 = scrapy.Field()
    #如下字段是被删除的字段，因为 喜马拉雅的返回的数据也在一直改变
    #formatted_created_at = scrapy.Field()
    #如下字段为发布的时间
    created_at = scrapy.Field()

    play_count = scrapy.Field()
    comments_count = scrapy.Field()
    shares_count = scrapy.Field()
    favorites_count = scrapy.Field()
    album_id = scrapy.Field()
    album_title = scrapy.Field()
    intro = scrapy.Field()
    #如下字段也被删除
    #time_until_now = scrapy.Field()
    category_name = scrapy.Field()
    category_title = scrapy.Field()

    #音频的标签内容
    tags = scrapy.Field()
    #上传者的姓名
    uploadUserName = scrapy.Field()


class QTCategory(scrapy.Item):
    collection = 'qt_category'
    s_type = 'qt_category'
    category_title = scrapy.Field()


class QTAudio(scrapy.Item):
    collection = 'qt_audio'
    s_type = 'qt_audio'
    category_title = scrapy.Field()
    sub_category_title = scrapy.Field()
    album_title = scrapy.Field()
    audioName = scrapy.Field()
    playUrl = scrapy.Field()


class QingtingAlbum(scrapy.Item):
    collection = 'qt_item'
    s_type = 'qt_item'
    contentSource = scrapy.Field()  #"www.qingting.fm"
    crawlType = scrapy.Field()  #"qt_album"
    category = scrapy.Field()   #总分类
    subcategory = scrapy.Field()    #子分类
    albumName = scrapy.Field()  #专辑名称
    albumPicUrl = scrapy.Field()    #专辑图片链接
    albumPicPath =scrapy.Field()    #专辑图片保存地址
    fullDescs = scrapy.Field()  #专辑介绍
    crawlTime = scrapy.Field()  #爬取时间
    audios = scrapy.Field() #专辑下节目列表
    albumUrl = scrapy.Field() # 专辑的url
