
jQuery.fn.paging = function(a) {
    return a = jQuery.extend({
        pageSize: 10,
        pageCount: 1,
        pageNum: 1,
        itemCount: 0,
        pageSpan: 3,
        callback: function() {
            return !1
        }
    }, a || {}), this.each(function() {
        function b() {
            c(), $(window).scrollTop(0), a.callback(a.pageNum)
        }

        function c() {
            if (a.pageCount > 1) {
                var b = '<div class="hl-page" style="text-align:center;"><a data-role="prev" ' + (1 === a.pageNum ? 'class="new-page-btn-disable"' : "") + " >&lt; 上一页</a>" + function() {
                    var b, c = [];
                    if (a.pageCount < 10)
                        for (b = 1; b <= a.pageCount; b++) c.push('<a data-role="goto" data-page="' + b + '" ' + (a.pageNum === b ? 'class="new-page-cur"' : "") + ">" + b + "</a>");
                    else if (a.pageNum <= a.pageSpan + 2) {
                        for (b = 1; b <= 2 * a.pageSpan + 1; b++) c.push('<a data-role="goto" data-page="' + b + '" ' + (a.pageNum === b ? 'class="new-page-cur"' : "") + ">" + b + "</a>");
                        c.push("...&nbsp;"), c.push('<a data-role="goto" data-page="' + a.pageCount + '">' + a.pageCount + "</a>")
                    } else if (a.pageNum >= a.pageCount - a.pageSpan - 2)
                        for (c.push('<a data-role="goto" data-page="1">1</a>'), c.push("...&nbsp;"), b = a.pageCount - 2 * a.pageSpan; b <= a.pageCount; b++) c.push('<a data-role="goto" data-page="' + b + '" ' + (a.pageNum === b ? 'class="new-page-cur"' : "") + ">" + b + "</a>");
                    else {
                        for (c.push('<a data-role="goto" data-page="1">1</a>'), c.push("...&nbsp;"), b = a.pageNum - a.pageSpan; b <= a.pageNum + a.pageSpan; b++) c.push('<a data-role="goto" data-page="' + b + '" ' + (a.pageNum === b ? 'class="new-page-cur"' : "") + ">" + b + "</a>");
                        c.push("...&nbsp;"), c.push('<a data-role="goto" data-page="' + a.pageCount + '">' + a.pageCount + "</a>")
                    }
                    return c.join("")
                }() + '<a data-role="next" ' + (a.pageNum === a.pageCount ? 'class="new-page-btn-disable"' : "") + ">下一页 &gt;</a></div>";
                d.html(b)
            }
        }


        var d = jQuery(this);
        d.off("click", "[data-role='prev']").on("click", "[data-role='prev']", function() {
            a.pageNum > 1 && (a.pageNum--, b())
        }), d.off("click", "[data-role='goto']").on("click", "[data-role='goto']", function() {
            var c = +$(this).attr("data-page");
            c !== a.pageNum && (a.pageNum = c, b())
        }), d.off("click", "[data-role='next']").on("click", "[data-role='next']", function() {
            a.pageNum < a.pageCount && (a.pageNum++, b())
        }), c()
    })
};


var s = {
    "code": "10000",
    "message": "success",
    "result": {
        "haveNext": 1,
        "nextPage": 2,
        "havePre": 0,
        "prePage": 1,
        "currentPage": 1,
        "totalPages": 130,
        "totalCounts": 3101,
        "pageSize": 24,
        "dataList": [{
            "id": 1100000003253,
            "type": 0,
            "name": "特种兵在都市",
            "comeFrom": "特种兵在都市",
            "comeFromId": null,
            "pic": "http://image.kaolafm.net/mz/images/201309/0d3e230c-1785-4b7d-90fd-abdc3f919707/default.jpg",
            "followedNum": 30655,
            "isOnline": 1,
            "listenNum": 10906946,
            "hasCopyright": 1,
            "desc": "原名《流氓艳遇记》，作者夜十三。背景深厚的少年杨洛，表面玩世不恭，立志做个流氓，私下里却为保卫国家安全而战。在执行任务的同时，漂亮的韩国美女，痞气十足的女教师，成熟性感的女总裁，清纯可爱的女明星纷纷被他吸引。最终他能否圆满完成任务，并抱得美人归？我们拭目以待。\r\n\r\n网友@永不逝去的微笑评论：难得的一本小说，主播声音也不错，很有感染力。",
            "host": [{
                "name": "刺儿",
                "des": "本名李振，声音性感，善于驾驭各种角色，声线多变；配音时擅长把握人物情绪。曾荣获天方听书网最受欢迎男播客称号。代表作有《全职高手》《流氓艳遇记》《黑道特种兵》《何以笙箫默》等。",
                "img": "http://image.kaolafm.net/mz/images/201411/e6f9866a-dee7-417e-b12d-1c400020ec65/default.jpg"
            }],
            "albumName": "特种兵在都市"
        }, {
            "id": 1100000002800,
            "type": 0,
            "name": "异世邪君",
            "comeFrom": "异世邪君",
            "comeFromId": null,
            "pic": "http://image.kaolafm.net/mz/images/201309/4b32b3b4-23a7-4220-b2d2-07a40fa39223/default.jpg",
            "followedNum": 21572,
            "isOnline": 1,
            "listenNum": 11413113,
            "hasCopyright": 1,
            "desc": "世间毁誉，世人冷眼，与我何干？以吾本性，快意恩仇！以吾本心，遨游世间！我命由我不由天！一代牛人穿越异界，看其踏上异世巅峰，成为一代邪君！\r\n\r\n",
            "host": [{
                "name": "夜风",
                "des": "有声小说播讲员。",
                "img": "http://image.kaolafm.net/mz/images/201412/9e5b13ea-11ce-46df-9fa0-fb85b06f360f/default.jpg"
            }],
            "albumName": "异世邪君"
        }, {
            "id": 1100000013060,
            "type": 0,
            "name": "天价小娇妻",
            "comeFrom": "天价小娇妻",
            "comeFromId": null,
            "pic": "http://image.kaolafm.net/mz/images/201505/c7273060-877f-4560-bff2-9bea8ca90554/default.jpg",
            "followedNum": 24273,
            "isOnline": 1,
            "listenNum": 10197287,
            "hasCopyright": 1,
            "desc": "“做我的情人，到我玩腻为止。”第一次见面，他强占她，逼她做情人。33日地狱般的索爱，沦为恶魔的禁脔。这是一场征服与反征服的游戏，谁先动情谁输，她输不起，唯一能守住的，只有自己的心...\r\n\r\n\r\n网友@紫色葡萄评论：真心好听的一本小说！好想嫁给男主角！",
            "host": [{
                "name": "德鲁伊",
                "des": "外表忠厚的生活机器，内心澎湃的声音叛逆。来吧，听听纯爷们的细腻！\r\n",
                "img": "http://image.kaolafm.net/mz/images/201405/25c89ee6-638d-4e02-86e6-aa765f8021ba/default.jpg"
            }, {
                "name": "语嫣",
                "des": "温暖、素装，这个清瘦的年轻女子，每每透着坚持的不可退让，铁马冰河波澜不惊，身体里面却藏着一股巨大的能量！",
                "img": "http://image.kaolafm.net/mz/images/201311/b846b3fb-0911-4039-8458-46925c5078ab/default.jpg"
            }],
            "albumName": "天价小娇妻"
        }, {
            "id": 1100000041040,
            "type": 0,
            "name": "极品女仙",
            "comeFrom": "极品女仙",
            "comeFromId": null,
            "pic": "http://image.kaolafm.net/mz/images/201412/5c2e5318-1c5d-4f52-af12-d8bc3cd84a59/default.jpg",
            "followedNum": 15603,
            "isOnline": 1,
            "listenNum": 7727120,
            "hasCopyright": 1,
            "desc": "一个现代女来到了一个陌生的世界，附身在一个被家族抛弃的家庭中，却因得到丹符宗的传承，踏上修仙路，一步一步建立起属于自己的领地，渐渐变成了一个神话，一个传说…\r\n\r\n网友@我爱小萝莉评论：节目超赞，最近一直在关注。",
            "host": [{
                "name": "御剑听风",
                "des": "知名有声小说播讲员。",
                "img": "http://image.kaolafm.net/mz/images/201603/5c7a59ea-47c8-49ed-8149-90a0ac4f3cf2/default.jpg"
            }, {
                "name": "筱梦",
                "des": "有声小说播讲员。",
                "img": "http://image.kaolafm.net/mz/images/201412/a04acb83-f381-421d-9e98-7c67b9767dd3/default.jpg"
            }],
            "albumName": "极品女仙"
        }, {
            "id": 1100000039155,
            "type": 0,
            "name": "校花的贴身高手",
            "comeFrom": "校花的贴身高手",
            "comeFromId": null,
            "pic": "http://image.kaolafm.net/mz/images/201412/9a2a53c3-eabd-4dec-a199-d7f4176c08c7/default.jpg",
            "followedNum": 15532,
            "isOnline": 1,
            "listenNum": 10055688,
            "hasCopyright": 1,
            "desc": "改编成网络剧后人气居高不下！\r\n普通的学生林逸身负追校花的任务，而且还是负校花老爸之命！长辈之命难违抗，林逸不得不给大小姐鞍前马后的当跟班…于是，史上最牛的跟班出现了！且看这位跟班如何发家致富偷小姐，开始他奉旨泡妞牛X闪闪的人生。这是一个大山里走出的绝世高手，一块能预知未来的神秘玉佩的故事，有点儿纯，也有点儿小暧昧…\r\n\r\n网友@蜂蜜番茄评论：小说确实不错，好想变成男主角啊！主播的声音也不错呢。\r\n",
            "host": [{
                "name": "御剑听风",
                "des": "知名有声小说播讲员。",
                "img": "http://image.kaolafm.net/mz/images/201603/5c7a59ea-47c8-49ed-8149-90a0ac4f3cf2/default.jpg"
            }],
            "albumName": "校花的贴身高手"
        }, {
            "id": 1100000000953,
            "type": 0,
            "name": "盗墓笔记1七星鲁王宫（周建龙）",
            "comeFrom": "盗墓笔记1七星鲁王宫（周建龙）",
            "comeFromId": null,
            "pic": "http://image.kaolafm.net/mz/images/201410/ccbb5682-c0ba-4347-93cd-b7ba49de12ec/default.jpg",
            "followedNum": 50716,
            "isOnline": 1,
            "listenNum": 1938233,
            "hasCopyright": 1,
            "desc": "五十年前，一群盗墓贼挖到了一部战国帛书，残书中记载了一个奇特的战国古墓位置，但也因为遭遇恐怖经历几乎全部身亡。五十年后，其中一个盗墓贼的孙子在先人笔记中发现了这个秘密，随即纠集了一批盗墓高手前去寻宝，但谁也没有想到，这个古墓隐藏了太多秘密…\r\n\r\n网友@我爱吴邪评论：就喜欢这个版本，别的跟这个一比都弱爆了。\r\n",
            "host": [{
                "name": "周建龙",
                "des": "著名有声小说播讲员，有“散仙”之称，播讲作品深受听众欢迎。毕业于解放军艺术学院，代表作有《鬼吹灯》《盗墓笔记》等。",
                "img": "http://image.kaolafm.net/mz/images/201406/8c96ed67-11b7-4db0-b4ab-02b87fd48f00/default.jpg"
            }],
            "albumName": "盗墓笔记1七星鲁王宫（周建龙）"
        }, {
            "id": 1100000003195,
            "type": 0,
            "name": "永生",
            "comeFrom": "永生",
            "comeFromId": null,
            "pic": "http://image.kaolafm.net/mz/images/201406/3700233f-005f-4376-8242-735407f74066/default.jpg",
            "followedNum": 10661,
            "isOnline": 1,
            "listenNum": 4520446,
            "hasCopyright": 1,
            "desc": "梦入神机作品。无穷无尽的新奇法宝，崭新世界，仙道门派，人妖神仙魔王皇帝，人间的爱恨情仇，恩怨纠葛，仙道的争斗法力，尽在永生。肉身、神通、长生、成仙、永生，一个卑微的生灵，怎样一步步走到这五重境界之巅，打开长生之门？\r\n\r\n网友@一米阳光评论：小说不错，写得很有感觉。读小说的主播也很强大！顶起！！\r\n",
            "host": [{
                "name": "晨诵无声",
                "des": "著名有声小说播音员，现居洛阳，以教书为生。声音浑厚，充满磁性，代表作有《斗罗大陆》 《三国重生之我是路人甲》《九鼎记》《天珠变》等。",
                "img": "http://image.kaolafm.net/mz/images/201405/7f75a86a-19bc-48c8-bd0d-8fb845d6f577/default.jpg"
            }],
            "albumName": "永生"
        }, {
            "id": 1100000013059,
            "type": 0,
            "name": "我当阴阳先生的那几年（景阳）",
            "comeFrom": "我当阴阳先生的那几年（景阳）",
            "comeFromId": null,
            "pic": "http://image.kaolafm.net/mz/images/201504/341bde45-ffc5-4826-b479-72df31d35827/default.jpg",
            "followedNum": 10354,
            "isOnline": 1,
            "listenNum": 2593536,
            "hasCopyright": 1,
            "desc": "因爷爷辈的恩怨，崔作非遭遇索命，溺水身亡，去到阴间，习得回魂之法。千辛万苦复活之后，为了完成师傅所托，崔作非成为一名白派阴阳先生，开始了和影响人类和谐的妖魔鬼怪斗争的漫漫长路…\r\n\r\n网友@蛋炒饭评论：真心不错，超级喜欢！",
            "host": [{
                "name": "景阳",
                "des": "有声小说播讲员。",
                "img": "http://image.kaolafm.net/mz/images/201503/d7231b91-26ad-4863-88b3-db1990e8d4fe/default.jpg"
            }],
            "albumName": "我当阴阳先生的那几年（景阳）"
        }, {
            "id": 1100000046405,
            "type": 0,
            "name": "最强弃少",
            "comeFrom": "最强弃少",
            "comeFromId": null,
            "pic": "http://image.kaolafm.net/mz/images/201502/1a78630a-83dc-4d06-a88c-5ce1f26724bb/default.jpg",
            "followedNum": 3907,
            "isOnline": 1,
            "listenNum": 14855324,
            "hasCopyright": 1,
            "desc": "豪门弃子重生，太空修炼重返地球。\r\n叶默蓦然清醒过来的时候，才发现周围的一切似乎都变了，美女师父也不见了。他也发现了自己成了被世家抛弃的弃子，但是这些都不重要，最重要的是他还记忆起了另外一件原本不属于他的可怕的事情。",
            "host": [{
                "name": "大鹏",
                "des": "大鹏，姓名刘鹏，１９８０年９月２日日出生于河北唐山。酷爱有声艺术，擅长模仿，希望做一名优秀的有声小说播讲者。",
                "img": "http://image.kaolafm.net/mz/images/201603/ba3f6fca-e56d-49ee-8a9b-035776331ff8/default.jpg"
            }],
            "albumName": "最强弃少"
        }, {
            "id": 1100000003291,
            "type": 0,
            "name": "狼性总裁",
            "comeFrom": "狼性总裁",
            "comeFromId": null,
            "pic": "http://image.kaolafm.net/mz/images/201409/ce322430-8af1-4e2c-a6d1-ef54da582c4e/default.jpg",
            "followedNum": 10645,
            "isOnline": 1,
            "listenNum": 2379399,
            "hasCopyright": 1,
            "desc": "渐渐的，她快要分不清这到底是赌局还是场失心的交易……他的正牌老婆\r\n突然从天而降，他在人前与老婆大秀恩爱，回过头却对她近似疯狂的掠取。明明不爱她，又霸道的不允许她身边出现除了他以外的男性生物！她受够了，她要逃走！她美好的人生绝对不允许一个叫费司爵的男人出现！\r\n\r\n网友@七仙女评论：小说写得还行，主播的声音确实不错！很有代入感，会一直关注的，",
            "host": [{
                "name": "萋萋",
                "des": "有声小说播讲员，青春甜美的女声。",
                "img": "http://image.kaolafm.net/mz/images/201410/83bcdfb8-f29f-4175-b539-75e9d9f847b8/default.jpg"
            }],
            "albumName": "狼性总裁"
        }, {
            "id": 1100000061872,
            "type": 0,
            "name": "百炼成仙",
            "comeFrom": "百炼成仙",
            "comeFromId": null,
            "pic": "http://image.kaolafm.net/mz/images/201507/6fa90252-6500-461f-a829-eec7d8b22155/default.jpg",
            "followedNum": 2934,
            "isOnline": 1,
            "listenNum": 9162348,
            "hasCopyright": 1,
            "desc": "讲述一个没有灵根的少年，机缘巧合，救了飘云谷一位重伤长老，对方感激，将他引荐入门，成为飘云谷这修真小门派的一员。又在机遇巧合之下得到变废为宝的能力，从此踏上了修仙的道路。仙路崎岖，百般磨练终成正果。一个没有灵根的少年，一个被认为是废物的家伙，在修真界不断地收购着各种废品……无论是废丹还是下品材料，来者不拒，有多少要多少！",
            "host": [{
                "name": "秦声",
                "des": "有声小说播讲员。",
                "img": "http://image.kaolafm.net/mz/images/201504/db23135a-e259-4b3d-bdf6-41e1d3aceb0b/default.jpg"
            }],
            "albumName": "百炼成仙"
        }, {
            "id": 1100000001344,
            "type": 0,
            "name": "花前月下：贪吃王妃",
            "comeFrom": "花前月下：贪吃王妃",
            "comeFromId": null,
            "pic": "http://image.kaolafm.net/mz/images/201410/e2581933-cfd9-4622-9a10-783442d01e5e/default.jpg",
            "followedNum": 9874,
            "isOnline": 1,
            "listenNum": 2449490,
            "hasCopyright": 1,
            "desc": "奚家结巴九小姐落水醒来后性情大变，她揍公主，挟天子，差点儿要了她丞相老爹的命。不久，丞相府门口一顶大红花轿落定，某男一笑：娘子，娶你虽非我本意，但是圣意难却，跟本王走吧！\r\n\r\n网友@眼镜蛇评论：真心不错，一直在关注。小说和主播都挺好的，建议大家都来听听。",
            "host": [{
                "name": "小夜光",
                "des": "",
                "img": "http://image.kaolafm.net/mz/images/201410/358c6d13-3fc8-4c23-aac5-921d9d838cd1/default.jpg"
            }],
            "albumName": "花前月下：贪吃王妃"
        }, {
            "id": 1100000000939,
            "type": 0,
            "name": "盗墓笔记2秦岭神树（周建龙）",
            "comeFrom": "盗墓笔记2秦岭神树（周建龙）",
            "comeFromId": null,
            "pic": "http://image.kaolafm.net/mz/images/201410/ccbb5682-c0ba-4347-93cd-b7ba49de12ec/default.jpg",
            "followedNum": 19191,
            "isOnline": 1,
            "listenNum": 1355215,
            "hasCopyright": 1,
            "desc": "朋友老痒出狱，带来诡异的六角铃铛。吴邪与老痒孤身深入到神秘莫测的秦岭探险，古老的厍族，巨大的青铜树，遥远的秦岭腹地…前方等待着他们的究竟是什么？\r\n\r\n网友@小哥评论：最喜欢周建龙版本的，再听一遍！推荐大家赶紧听听！\r\n\r\n",
            "host": [{
                "name": "周建龙",
                "des": "著名有声小说播讲员，有“散仙”之称，播讲作品深受听众欢迎。毕业于解放军艺术学院，代表作有《鬼吹灯》《盗墓笔记》等。",
                "img": "http://image.kaolafm.net/mz/images/201406/8c96ed67-11b7-4db0-b4ab-02b87fd48f00/default.jpg"
            }],
            "albumName": "盗墓笔记2秦岭神树（周建龙）"
        }, {
            "id": 1100000012596,
            "type": 0,
            "name": "总裁的替身前妻",
            "comeFrom": "总裁的替身前妻",
            "comeFromId": null,
            "pic": "http://image.kaolafm.net/mz/images/201309/dbeffd31-2ab9-4fa1-b50b-43cc45da17a1/default.jpg",
            "followedNum": 9829,
            "isOnline": 1,
            "listenNum": 2826376,
            "hasCopyright": 1,
            "desc": "那一夜，她醉得朦胧，他一夜索取，不知厌倦，她不知身上的男人是谁，她迷失了方向，是熟悉的他，还是陌生的男人？\r\n\r\n网友@泡沫之夏评论：男生爱，女生更爱的小说。强烈推荐！",
            "host": [{
                "name": "糖糖",
                "des": "有声小说播讲员，代表作《总裁的替身前妻》。",
                "img": "http://image.kaolafm.net/mz/images/201506/ab87d285-038f-401b-b0b5-af5fc4884dd7/default.jpg"
            }],
            "albumName": "总裁的替身前妻"
        }, {
            "id": 1100000001142,
            "type": 0,
            "name": "绣花毒后",
            "comeFrom": "绣花毒后",
            "comeFromId": null,
            "pic": "http://image.kaolafm.net/mz/images/201410/d774b557-770b-4809-a269-521ff8be1715/default.jpg",
            "followedNum": 10121,
            "isOnline": 1,
            "listenNum": 1974043,
            "hasCopyright": 1,
            "desc": "什么！她只不过是喊一句“菠萝菠萝蜜”就魂穿了？还穿到一个走三步喘百下大字不识的皇后身上？听说皇后是被蜈蚣吓死的。可在一次后宫嫔妃，文武大臣集聚的宴席上，是谁居心叵测在她盘里放一只蜈蚣？想吓她还太早了吧，筷子一夹，吩咐太监：“这是上好的中药，别浪费了，快收起来以后可以吃。”深宫就是个祸害人的地方，她竟被下了药！动弹不得时，听天由命的看着进来的男人是哪位？老天保佑一定要来个俊的\r\n\r\n网友@建宁公主评论：一直都在听这个小说，真的很不错呢！",
            "host": [{
                "name": "书友佳苑",
                "des": "有声小说播讲员，充满活力又不失稳重的女声。",
                "img": "http://image.kaolafm.net/mz/images/201411/bd5d2c07-0d3d-496c-8feb-6b990e0e3f13/default.jpg"
            }],
            "albumName": "绣花毒后"
        }, {
            "id": 1100000049915,
            "type": 0,
            "name": "仙侠奇缘之花千骨（果果）",
            "comeFrom": "仙侠奇缘之花千骨（果果）",
            "comeFromId": null,
            "pic": "http://image.kaolafm.net/mz/images/201506/b5a3ec85-94d4-4dd1-b233-6e114ebb13f6/default.jpg",
            "followedNum": 19483,
            "isOnline": 1,
            "listenNum": 2294543,
            "hasCopyright": 1,
            "desc": "她是世间最后一个神，出生时满城鲜花尽凋零，故取名花千骨；他是守护着天下苍生的长留上仙，淡然而带着冰冷的目光，流泄如水如月华。\r\n\r\n\r\n网友@聂小倩评论;节目太棒了，爱死花千骨了，小说写得好，主播表现的也很好！",
            "host": [{
                "name": "卿语",
                "des": "",
                "img": "http://image.kaolafm.net/mz/images/201508/c077071b-5c90-4556-83b5-1aebb22ff2d2/default.jpg"
            }],
            "albumName": "仙侠奇缘之花千骨（果果）"
        }, {
            "id": 1100000001931,
            "type": 0,
            "name": "回到明朝当王爷",
            "comeFrom": "回到明朝当王爷",
            "comeFromId": null,
            "pic": "http://image.kaolafm.net/mz/images/201409/99434c27-9033-4c7d-baae-bfab86c14c32/default.jpg",
            "followedNum": 18603,
            "isOnline": 1,
            "listenNum": 2873935,
            "hasCopyright": 1,
            "desc": "月关作品。阴差阳错间，乌龙九世善人郑少鹏回到了大明正德年间。那是一个多姿多彩的时代，既有京师八虎的邪恶，又有江南四大才子的风流，还有大儒王阳明的心学和东厂、西厂、锦衣卫的纷争，再加上荒诞不经的正德皇帝朱厚照。浑浑噩噩中踏进这个时代，不得不为了自己的命运，周旋在这形形色色的人物之中…",
            "host": [{
                "name": "巴胡子",
                "des": "知名有声小说播讲员，声音沧桑、稳重又不是诙谐幽默，极具特色。深受广大听友喜爱。",
                "img": "http://image.kaolafm.net/mz/images/201602/5ee07aff-5dad-482d-b1a2-8e1551fab756/default.jpg"
            }],
            "albumName": "回到明朝当王爷"
        }, {
            "id": 1100000001397,
            "type": 0,
            "name": "傲神",
            "comeFrom": "傲神",
            "comeFromId": null,
            "pic": "http://image.kaolafm.net/mz/images/201410/3414c4e6-1a5a-4437-a15b-8b51130e6d20/default.jpg",
            "followedNum": 6510,
            "isOnline": 1,
            "listenNum": 2635647,
            "hasCopyright": 1,
            "desc": "一纸休书，亲家成仇家，手持神琴“青殇”，魂天八曲一出，青天为之色变，身兼两大法则，在这法则林立的修真世界之中，且看他是如何一步步迈向巅峰。\r\n\r\n\r\n网友@双双评论：很喜欢这本小说，会继续关注的。主持人加油更新啊，等不及了！",
            "host": [{
                "name": "兔哥哥",
                "des": "有声小说播讲员，代表作《傲神》。",
                "img": "http://image.kaolafm.net/mz/images/201510/7c327ad9-8b09-45f1-81cb-39192662ae52/default.jpg"
            }],
            "albumName": "傲神"
        }, {
            "id": 1100000001736,
            "type": 0,
            "name": "超级仙医（晨诵无声版）",
            "comeFrom": "超级仙医（晨诵无声版）",
            "comeFromId": null,
            "pic": "http://image.kaolafm.net/mz/images/201410/91a49748-aaf7-432c-aba6-0cca46c92a91/default.jpg",
            "followedNum": 9961,
            "isOnline": 1,
            "listenNum": 2563202,
            "hasCopyright": 1,
            "desc": "他，是雍城大学校医院的菜鸟校医，刚刚毕业踏入社会，他，是医术精湛、活人无数的仙医，中西医，无所不精。",
            "host": [{
                "name": "晨诵无声",
                "des": "著名的有声小说播音员，现居洛阳，以教书为生。代表作：《斗罗大陆》 《三国重生之我是路人甲》《九鼎记》《天珠变》等。",
                "img": "http://image.kaolafm.net/mz/images/201404/54ea5d92-0efd-4eb1-904b-87ba4708cd1f/default.jpg"
            }],
            "albumName": "超级仙医（晨诵无声版）"
        }, {
            "id": 1100000067434,
            "type": 0,
            "name": "很纯很暧昧",
            "comeFrom": "很纯很暧昧",
            "comeFromId": null,
            "pic": "http://image.kaolafm.net/mz/images/201508/dafd9b57-7394-495c-bfaf-f8e80e0000a8/default.jpg",
            "followedNum": 2683,
            "isOnline": 1,
            "listenNum": 6847533,
            "hasCopyright": 1,
            "desc": "杨明本是一名普通的高中生，一次意外让他获得了一副神奇的眼镜，这眼睛戴上以后不但可以自动调焦，可以透视！而且竟然还能看清别人的想法！多姿多彩的生活一下子降临在了杨明的身上，真是无往不利！",
            "host": [{
                "name": "刘大明白",
                "des": "有声小说播讲员。",
                "img": "http://image.kaolafm.net/mz/images/201504/ced042ed-443b-4260-b0ab-682c6a8d192b/default.jpg"
            }],
            "albumName": "很纯很暧昧"
        }, {
            "id": 1100000000930,
            "type": 0,
            "name": "盗墓笔记3云顶天宫（周建龙）",
            "comeFrom": "盗墓笔记3云顶天宫（周建龙）",
            "comeFromId": null,
            "pic": "http://image.kaolafm.net/mz/images/201510/f5bfdc9c-48aa-4753-86c9-e3168df86ac5/default.jpg",
            "followedNum": 14540,
            "isOnline": 1,
            "listenNum": 1055209,
            "hasCopyright": 1,
            "desc": "十年前，顺子的父亲带领一批神秘人进入茫茫雪山，闯入凶险莫名的地宫墓室，发现了数不胜数的金银财宝，但他们却全部死于非命。十年后，吴邪一行和顺子一行人再次踏足云顶天宫，这更是一次直逼死亡的惊险大穿越……\r\n\r\n\r\n网友@小肚肚评论：我一直听，超棒的！",
            "host": [{
                "name": "周建龙",
                "des": "著名有声小说播讲员，有“散仙”之称，播讲作品深受听众欢迎。毕业于解放军艺术学院，代表作有《鬼吹灯》《盗墓笔记》等。",
                "img": "http://image.kaolafm.net/mz/images/201406/8c96ed67-11b7-4db0-b4ab-02b87fd48f00/default.jpg"
            }],
            "albumName": "盗墓笔记3云顶天宫（周建龙）"
        }, {
            "id": 1100000046404,
            "type": 0,
            "name": "天才狂妃：废物三小姐",
            "comeFrom": "天才狂妃：废物三小姐",
            "comeFromId": null,
            "pic": "http://image.kaolafm.net/mz/images/201502/389e3408-fd46-4dc4-a473-03f8429fb959/default.jpg",
            "followedNum": 6168,
            "isOnline": 1,
            "listenNum": 2059938,
            "hasCopyright": 1,
            "desc": "她本是顶尖特工，因一次追杀误入陌生国度，成为落家三小姐。爹爹不疼，大娘不爱，嫡姐欺凌，未婚夫挑衅。她冷然一笑，都放马过来吧，老娘奉陪！三年隐忍，十年伪装，一朝重生，颠倒天下！翻云覆雨，指鹿为马，斗得人仰马翻哀嚎一片，这……当真是那废物？",
            "host": [{
                "name": "如水",
                "des": "有声小说播讲员。",
                "img": "http://image.kaolafm.net/mz/images/201503/4cc2e44d-b6d2-4620-a9f6-ea4523571ae9/default.jpg"
            }],
            "albumName": "天才狂妃：废物三小姐"
        }, {
            "id": 1100000000460,
            "type": 0,
            "name": "鬼吹灯Ⅰ之1精绝古城",
            "comeFrom": "鬼吹灯Ⅰ之1精绝古城",
            "comeFromId": null,
            "pic": "http://image.kaolafm.net/mz/images/201409/02b03922-ca24-4b2d-86c5-738a23e4bfe7/default.jpg",
            "followedNum": 14489,
            "isOnline": 1,
            "listenNum": 1091832,
            "hasCopyright": 1,
            "desc": "鬼吹灯电影版原著。胡八一和好友胖子加入了一支前往新疆的考古队。一行人历经万险来到塔克拉玛干沙漠中的精绝古城遗址，进入了地下鬼洞。洞中机关重重、陷阱不断，这神秘的鬼洞似乎在先知的掌控之中……\r\n作者天下霸唱，原名张牧野，生于七十年代，天津人氏，其作品《鬼吹灯》系列风靡华语世界。",
            "host": [{
                "name": "周建龙",
                "des": "著名有声小说播讲员，有“散仙”之称，播讲作品深受听众欢迎。毕业于解放军艺术学院，代表作有《鬼吹灯》《盗墓笔记》等。",
                "img": "http://image.kaolafm.net/mz/images/201406/8c96ed67-11b7-4db0-b4ab-02b87fd48f00/default.jpg"
            }],
            "albumName": "鬼吹灯Ⅰ之1精绝古城"
        }, {
            "id": 1100000000897,
            "type": 0,
            "name": "盗墓笔记4蛇沼鬼城（周建龙）",
            "comeFrom": "盗墓笔记4蛇沼鬼城（周建龙）",
            "comeFromId": null,
            "pic": "http://image.kaolafm.net/mz/images/201510/2c4170a4-70f7-42b0-bcd3-d03e02680c0c/default.jpg",
            "followedNum": 12899,
            "isOnline": 1,
            "listenNum": 949258,
            "hasCopyright": 1,
            "desc": "通过和三叔长谈，吴邪了解到二十年前海底古墓里的隐情。两盘来自张起灵的录像带让事情陷入重重迷雾。循着录像带的线索，吴邪只身来到青海……\r\n《盗墓笔记》系列是南派三叔的代表作，与《鬼吹灯》共同开启了中国通俗小说界的盗墓时代。堪称中国出版界的神作，获得百万读者狂热追捧，盛赞不断。南派三叔也凭借此书作名满天下。\r\n",
            "host": [{
                "name": "周建龙",
                "des": "著名有声小说播讲员，有“散仙”之称，播讲作品深受听众欢迎。毕业于解放军艺术学院，代表作有《鬼吹灯》《盗墓笔记》等。",
                "img": "http://image.kaolafm.net/mz/images/201406/8c96ed67-11b7-4db0-b4ab-02b87fd48f00/default.jpg"
            }],
            "albumName": "盗墓笔记4蛇沼鬼城（周建龙）"
        }],
        "facet": [{
            "facetFiled": "type",
            "facetCountMap": {
                "10000": 0,
                "20000": 3101,
                "30000": 224984
            }
        }]
    },
    "serverTime": 1457335293385
}

