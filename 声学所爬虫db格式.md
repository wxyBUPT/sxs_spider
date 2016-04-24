#数据库格式（原始数据部分）

##考拉fm

###1、考拉类别信息
```
{
	"_id" : ObjectId("571a1447e138237497458fd8"),
	"sourceUrl" : "http://www.kaolafm.com/category/1165",
	"categoryName" : "军事",
	"pageSize" : 24,
	"totalCounts" : 69,
	"subCategorys" : [
		{
			"linkType" : 1,
			"categoryName" : "军情速递",
			"hasSub" : 0,
			"imageAoyo" : "",
			"categoryId" : 1314,
			"imageAoyoEffect" : "",
			"logo" : "http://image.kaolafm.net/mz/images/201603/3fff5ffd-d6a4-437c-90c3-44b49494c59e/default.jpg",
			"id" : -1
		},
		{
			"linkType" : 1,
			"categoryName" : "军史档案",
			"hasSub" : 0,
			"imageAoyo" : "",
			"categoryId" : 1315,
			"imageAoyoEffect" : "",
			"logo" : "http://image.kaolafm.net/mz/images/201603/7166226b-bddf-4fb1-a417-168db80bacbe/default.jpg",
			"id" : -1
		},
		{
			"linkType" : 1,
			"categoryName" : "武器装备",
			"hasSub" : 0,
			"imageAoyo" : "",
			"categoryId" : 1313,
			"imageAoyoEffect" : "",
			"logo" : "http://image.kaolafm.net/mz/images/201603/deb0658e-4407-4614-b1bf-a82df010f2d5/default.jpg",
			"id" : -1
		}
	],
	"totalPages" : 3,
	"categoryId" : 1165
}
```  

* _id ：主键
* sourceUrl：类别在考拉网站的url
* categoryName：类别名称
* pageSize：类别一页的专辑数目
* totalCounts 类别下总页数
* subCategorys 子类别
* categoryName：子类别名称
* logo ：子类别logo url
* categoryId：子类别Id


***
###2、考拉网站专辑
```
{
	"_id" : ObjectId("571a148ae138237497458fef"),
	"pageSize" : 20,
	"audios" : [
		{
			"audioId" : NumberLong("1000002233810"),
			"playUrl" : "http://image.kaolafm.net/mz/outopus_16/201602/28010074-86d8-4e66-932f-737a3ec63154.opus"
		},
		{
			"audioId" : NumberLong("1000002233813"),
			"playUrl" : "http://image.kaolafm.net/mz/outopus_16/201602/a308d101-8dbd-45a1-baf3-719cd7f2850a.opus"
		},
		{
			"audioId" : NumberLong("1000002233844"),
			"playUrl" : "http://image.kaolafm.net/mz/outopus_16/201602/9bd44ce2-9ff4-41e2-b446-9c15793e56c7.opus"
		},
		{
			"audioId" : NumberLong("1000002233847"),
			"playUrl" : "http://image.kaolafm.net/mz/outopus_16/201602/0c42b3d3-421e-4c26-a9ed-5c9c304219ae.opus"
		},
		{
			"audioId" : NumberLong("1000002233901"),
			"playUrl" : "http://image.kaolafm.net/mz/outopus_16/201602/b8dba548-deb5-488a-bbcd-57465746240f.opus"
		},
		{
			"audioId" : NumberLong("1000002233919"),
			"playUrl" : "http://image.kaolafm.net/mz/outopus_16/201602/1116158e-4fe7-48ca-b5f8-14e95912de00.opus"
		},
		{
			"audioId" : NumberLong("1000002256643"),
			"playUrl" : "http://image.kaolafm.net/mz/outopus_16/201602/bdda8b4e-622c-4a87-8a15-932b85397a0c.opus"
		},
		{
			"audioId" : NumberLong("1000002280876"),
			"playUrl" : "http://image.kaolafm.net/mz/outopus_16/201603/62d6d392-2a91-4f0d-b09d-3e06c6e2a967.opus"
		},
		{
			"audioId" : NumberLong("1000002296060"),
			"playUrl" : "http://image.kaolafm.net/mz/outopus_16/201603/73f0d359-40e8-4b3d-ba0a-0ebc5ef640a9.opus"
		},
		{
			"audioId" : NumberLong("1000002330497"),
			"playUrl" : "http://image.kaolafm.net/mz/outopus_32/201603/0169223d-7b6c-4b07-a5c1-ab656e073aa7.opus"
		}
	],
	"commentCount" : 0,
	"shortDesc" : "岁月留声，光阴永存！",
	"albumPicUrl" : "http://image.kaolafm.net/mz/images/201602/1d5ab80e-b2ce-4101-a8be-67d74efd9782/default.png",
	"categoryName" : "公益",
	"index" : 22,
	"fullDescs" : "岁月留声，光阴永存！",
	"followedNum" : 6,
	"categoryPage" : 6,
	"lastModifyTime" : ISODate("2016-04-22T20:09:44.368Z"),
	"type" : 0,
	"categoryId" : 994,
	"status" : "更新中",
	"anchors" : [
		{
			"des" : "",
			"name" : "月上岚",
			"img" : ""
		}
	],
	"tags" : [
		"光音工坊",
		"月上岚",
		"CV",
		"广播剧",
		"配音"
	],
	"audioCounts" : 10,
	"comeFromId" : null,
	"comeFrom" : "光音工坊",
	"albumId" : NumberLong("1100000117692"),
	"produce" : "用户分享 ",
	"uploaderId" : 2490178,
	"updateDay" : "不定期更新",
	"uploadUserName" : "月上岚",
	"listenNum" : 14006,
	"shareUrl" : "http://m.kaolafm.com/share/zj.html?albumId=1100000117692",
	"albumName" : "光音工坊",
	"sumPage" : 1
}
```

* audioCount： 音频总数
* commentCount：被评论的次数
* shortDesc：简单描述
* albumPicUrl：音频封面url
* categoryName：类别名称
* index：类别在对应category 下的第几页
* fullDescs：完整描述
* followedNum：订阅专辑的人数
* lastModifyTime：音频最后更新时间
* categoryId：类别Id
* status：音频状态
* anchors：上传者信息
* tags：音频文件标签
* comeFrom：音频来源
* albumId：在考拉中对应的albumId
* produce：音频途径
* uploaderId：上传人Id
* updateDay：什么时候上传
* uploadUserName：上传者姓名
* listenNum：播放次数
* shareUrl：分享url
* albumName：专辑名称
* sumPage：专辑中歌曲页数
* _id：主键
* audios：音频简略信息

***
###3、考拉网站的音频
```
{
	"_id" : ObjectId("571a1488e138237497458fe5"),
	"updateTime" : "2016-02-05",
	"uploaderName" : "月上岚",
	"duration" : 237976,
	"uuid" : "19ae59de088311e699c0782bcb3b9846",
	"crawledCount" : 1,
	"crawledTime" : ISODate("2016-04-22T20:09:44.597Z"),
	"createTime" : NumberLong("1454638740000"),
	"orderNum" : 1,
	"audioPicUrl" : null,
	"sendToCNRTime" : null,
	"audioId" : NumberLong("1000002233810"),
	"likedNum" : 0,
	"commentNum" : 0,
	"m3u8PlayUrl" : "http://image.kaolafm.net/mz/aac_64/201602/28010074-86d8-4e66-932f-737a3ec63154/playlist.m3u8",
	"fileSize" : 1863117,
	"uploaderId" : 2490178,
	"mp3PlayUrl" : "http://image.kaolafm.net/mz/audios/201602/28010074-86d8-4e66-932f-737a3ec63154.mp3",
	"playUrl" : "http://image.kaolafm.net/mz/outopus_16/201602/28010074-86d8-4e66-932f-737a3ec63154.opus",
	"audioDesc" : null,
	"audioName" : "校园灵异广播剧——《轮回》（片花）",
	"listenNum" : 866,
	"audioDownloadDir" : "/var/crawler/kl/audios/full/90f4be0f22dd148698d09d5fad1556ff2bda6a07.m3u8",
	"shareUrl" : "http://m.kaolafm.com/share/jm.html?audioId=1000002233810",
	"accPlayUrl" : null,
	"album_title" : "光音工坊",
	"checksum" : "d68260612135cc53cb15d498fd338ec9"
}
```

* updateTime：专辑更新时间
* uploaderName：音频上传者
* duration：音频持续时间
* uuid：音频的uuid，与给cnr 的uuid 相同，同时也根据uuid 来寻找对应的音频
* crawledCount：音频被爬虫爬取的次数
* crawledTime：音频首次被爬虫获得的时间
* createTime：音频在考拉网站中首次被创建的时间
* orderNum：顺序
* audioPicUrl：音频封面的url
* sendToCNRTime：音频被发送到CNR 的时间，如果为空则代表没有被发送到CNR
* audioId：音频在考拉网站的id
* likedNum：音频在原来网站中被喜欢的次数
* commentNum：音频在原来网站中被评论的次数
* m3u8PlayUrl：音频在原网站中的m3u8 的播放地址
* fileSize：音频文件的大小
* uploaderId：音频上传者的姓名
* mp3PlayUrl：音频MP3播放地址
* playUrl：音频播放地址
* audioDesc：音频的描述
* audioName：音频名称
* listenNum：音频被收听的次数
* audioDownloadDir：当前音频被下载的路径，如果为空则代表未下载，未下载的音频不会被推送到cnr
* shareUrl：音频在原始网站中分享的url
* accPlayUrl：使用acc 格式播放的地址
* album_title:音频所属的album 名称
* checksum：下载音频的md5值，如果音频未被下载，则为空

##喜马拉雅fm

###1、喜马拉雅类别
```
{
	"_id" : ObjectId("571a2dfce1382377590c23ce"),
	"cid" : "3",
	"href" : "http://www.ximalaya.com/dq/book/",
	"nameText" : "有声书",
	"subCategorys" : [
		"言情",
		"悬疑",
		"幻想",
		"历史",
		"都市",
		"文学",
		"社科",
		"武侠",
		"读客图书",
		"QQ阅读",
		"果麦文化",
		"中信出版",
		"博集天卷",
		"速播专区",
		"推理世界",
		"正能量有声书"
	],
	"cname" : "book"
}
```

* _id：主键
* cid：category id
* href：在原来网站中category 的地址
* nameText：在原来网站中的名称
* subCategorys：类别包含的子类别
* cname：categoryName

***
###2、喜马拉雅网站的专辑信息
```
{
	"_id" : ObjectId("571a2e0fe1382377590c23fa"),
	"categoryName" : "【商业财经】",
	"imgSrc" : "http://fdfs.xmcdn.com/group8/M01/74/FD/wKgDYFX-z1XAbxRIAAEx5osVmk0793_web_large.jpg",
	"tags" : [
		"财经资讯",
		"财经评论",
		"创业密码",
		"商业聚焦",
		"股指期货"
	],
	"crawledCount" : 1,
	"album_id" : "2983857",
	"audios" : [
		{
			"id" : "8850477",
			"album_id" : 2983857
		}
	],
	"uploadUserName" : "\r\n            管理之声\r\n            ",
	"crawledTime" : ISODate("2016-04-22T21:58:39.106Z"),
	"href" : "http://www.ximalaya.com/29947683/album/2983857",
	"albumDesc" : "企业家自己的故事。",
	"uploadUserUrl" : "http://www.ximalaya.com/zhubo/29947683/",
	"playTime" : "177",
	"album_name" : "企业家"
}
```

* _id ：索引id
* categoryName：类别名称
* imgSrc：类别在原来网站中的封面url信息
* tags：类别所属的标签
* crawledCount：本专辑被爬虫爬取的次数
* album_id:album 在喜马拉雅网站中原始的id
* audio：在喜马拉雅中这个专辑拥有的歌曲的简单的描述
* uploadUserName：专辑上传者姓名
* crawledTime：专辑被爬虫第一次爬取的时间
* href：专辑在原始网站中的链接
* albumDesc：专辑的描述
* uploadUserUrl：专辑上传者的url
* playTime：专辑被播放的次数
* album_name：专辑的名称

***
###3、音频信息

```
{
	"_id" : ObjectId("571a2e0ce1382377590c23e6"),
	"uid" : 4253278,
	"album_id" : 389451,
	"audioChecksum" : null,
	"intro" : "",
	"play_path_32" : "http://audio.xmcdn.com/group11/M00/37/78/wKgDa1WWnp7CUK4SAEMm6D8va3k417.m4a",
	"duration" : 1452,
	"id" : "6447415",
	"uuid" : "4f2a32e0089211e69dce782bcb3b9846",
	"title" : "张少佐评书黄杨传001",
	"crawledCount" : 1,
	"sendToCNRTime" : null,
	"upload_id" : "u_5463419",
	"cover_url" : "http://fdfs.xmcdn.com/group6/M07/4D/47/wKgDg1U0543TKCnMAAEAFfU4hWc143.jpg",
	"play_count" : 3706,
	"uploadUserName" : "\r\n            惜林槐香\r\n            ",
	"cover_url_142" : "http://fdfs.xmcdn.com/group6/M07/4D/47/wKgDg1U0543TKCnMAAEAFfU4hWc143_web_large.jpg",
	"play_path_64" : "http://audio.xmcdn.com/group11/M00/37/80/wKgDbVWWnmDgH23vAFlLABTtPbA323.m4a",
	"nickname" : "惜林槐香",
	"category_name" : "comic",
	"shares_count" : 0,
	"favorites_count" : 12,
	"play_path" : "http://audio.xmcdn.com/group11/M00/37/80/wKgDbVWWnmDgH23vAFlLABTtPbA323.m4a",
	"created_at" : ISODate("2015-04-20T00:00:00Z"),
	"audioDownloadDir" : "/var/crawler/xmly/audios/full/412b8fd00600331c1d6492624cde21076618b3b4.m4a",
	"crawledTime" : ISODate("2016-04-22T21:58:36.779Z"),
	"comments_count" : 5,
	"album_title" : "张少佐《黄杨传》",
	"category_title" : "相声评书",
	"checksum" : "146b12a9635b0c55ccadcccec0a5ce2b"
}
```

* _id : 音频的索引
* uid ： 音频上传者的id 
* album_id：音频所属的album 的id
* audioChecksum：所下载的音频文件的校验和，如果音频文件未被下载则校验和为空
* intro：音频简单的描述信息
* play_path_32 ： 音频32 位的播放地址
* duration：音频的持续时间
* id：音频的id
* uuid：音频的uuid ，uuid 为与央广传递唯一地址的地方，uuid 不会被改变
* title 音频名称
* crawledCount：音频被爬虫获得元信息的次数
* sendToCNRTime 音频被发送的cnr 时间，如果为空则代表音频未被发送到cnr
* upload_id 上传者的id
* cover_url 封面的url
* paly_count 音频被播放的次数
* uploadUserName 音频上传者的名称
* cover_url_142 音频封面的url
* paly_path_64 音频的64 位播放地址
* nickname 音频上传者的姓名
* category_name 音频所属category 的英文名称
* shares_count  音频被分享的次数
* favorites_counts 音频被喜欢的次数
* paly_path 音频的播放地址
* created_at 音频被创建的时间
* audioDownloadDir 音频被下载的本地位置，如果为空则代表音频尚未被下载
* crawldeTime 音频首次被爬虫下载元数据的时间
* comments_count 音频的评论次数
* album_title 音频所属album 的名称
* category_title 音频所属的category 的名称
* checksum 如果音频被下载，则此字段代表音频的校验和，如果音频未被下载则没有此字段



##蜻蜓fm

###1、蜻蜓fm 的专辑信息
```
{
	"_id" : ObjectId("571a12d4e138237180c34984"),
	"category" : " 音乐 ",
	"subcategory" : "精选·专题",
	"contentSource" : "www.qingting.fm",
	"crawledCount" : 1,
	"fullDescs" : "None",
	"albumName" : "年代FM",
	"audios" : [
		{
			"album_title" : "年代FM",
			"audioName" : "70后怀旧金曲",
			"sub_category_title" : "精选·专题",
			"category_title" : " 音乐 ",
			"playUrl" : "http://od.qingting.fm/live/3911402.m3u8"
		},
		{
			"album_title" : "年代FM",
			"audioName" : "80后爱听的歌",
			"sub_category_title" : "精选·专题",
			"category_title" : " 音乐 ",
			"playUrl" : "http://od.qingting.fm/live/3999089.m3u8"
		},
		{
			"album_title" : "年代FM",
			"audioName" : "90后爱听的歌",
			"sub_category_title" : "精选·专题",
			"category_title" : " 音乐 ",
			"playUrl" : "http://od.qingting.fm/live/3999976.m3u8"
		}
	],
	"crawledTime" : ISODate("2016-04-22T20:02:28.808Z"),
	"albumPicPath" : "",
	"crawlType" : "qt_album",
	"albumPicUrl" : "http://pic.qingting.fm/2015/0805/20150805111256939.jpg!400",
	"crawlTime" : "2016-04-22 20:02:28"
}
```

* _id 唯一索引
* category 所属类别
* subcategory 所属子类别
* contentSource 内容来源
* crawledCount 专辑被爬虫爬取的次数
* fullDescs 音频完整的描述
* albumName 专辑名称
* audios 专辑中所包含的所有音频
* crawledTime 专辑被爬虫第一次爬取的时间
* albumPicUrl 专辑封面的url
* crawltime 专辑第一次被爬取的时间


***
###2、qt 音频
```
{
	"_id" : ObjectId("5719f56ee1382364a6740310"),
	"audioName" : "大明演义 第1回",
	"uuid" : "900655fe087011e68619782bcb3b9846",
	"crawledCount" : 2,
	"audioDownloadDir" : "/var/crawler/qt/audios/full/426e12396136ca0dd1ed227ba9d3bf6918028b8d.m4a",
	"sub_category_title" : "评书演义",
	"crawledTime" : ISODate("2016-04-22T17:57:02.707Z"),
	"sendToCNRTime" : null,
	"album_title" : "单田芳评书：大明演义",
	"category_title" : " 历史 ",
	"playUrl" : "http://od.qingting.fm/vod/00/00/0000000000000000000026028559_64.m4a",
	"checksum" : "75b8326d258b1834c68f704d1b9ee16c"
}
```

* _id 唯一索引
* audioName 音频名称
* uuid 唯一标识，次标识也是通过接口传递个cnr 的唯一资源定位标识
* crawledCount 音频被爬虫获得元数据的次数
* audioDownloadDir 音频文件被下载到本地的地址，如果为空则代表音频文件尚未被下砸
* sub_category_title 音频所属子类别的名称
* crawledTime 音频第一次被爬虫下载元数据的时间
* sendToCNRTime 音频被发送到cnr 的时间，如果为空，则代表当前音频未被发送到cnr
* album_title 音频所属的专辑
* category_title 音频所属的类别
* playUrl 音频播放地址
* checksum 本地现在音频的校验和，如果音频未被下载则校验和为null
