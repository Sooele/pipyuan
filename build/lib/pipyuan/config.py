cmd_pip: list = ["python", "-m", "pip"]
cmd_pip_getY: list = cmd_pip + ["config", "get", "global.index-url"]


yuanList = {
    "gf": {
        "cmd": "gf",
        "name": "官方",
        "url": "https://pypi.org/simple/"
    },
    "a": {
        "cmd": "a",
        "name": "阿里云",
        "url": "https://mirrors.aliyun.com/pypi/simple/"
    },
    "q": {
        "cmd": "q",
        "name": "清华",
        "url": "https://pypi.tuna.tsinghua.edu.cn/simple"
    },
    "t": {
        "cmd": "t",
        "name": "腾讯",
        "url": "https://mirrors.cloud.tencent.com/pypi/simple"
    },
    "h": {
        "cmd": "h",
        "name": "华为",
        "url": "https://mirrors.huaweicloud.com/repository/pypi/simple/"
    },
    "d": {
        "cmd": "d",
        "name": "豆瓣",
        "url": "https://pypi.douban.com/simple/"
    },

    # 内网
    "tn": {
        "cmd": "tn",
        "name": "腾讯内网",
        "url": "https://mirrors.tencentyun.com/pypi/simple"
    },
    "an": {
        "cmd": "an",
        "name": "阿里内网",
        "url": "https://mirrors.aliyuncs.com/pypi/simple/"
    },
    "hn": {
        "cmd": "hn",
        "name": "华为内网",
        "url": "https://mirrors.myhuaweicloud.com/pypi/web/simple"
    }


}
