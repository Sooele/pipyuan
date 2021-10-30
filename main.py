
import sys
import textwrap
import os
import gettext

def my_i18n(Text:str):
    Text = Text.replace("usage", "用法")
    Text = Text.replace("show this help message and exit",
                        "查看帮助")
    Text = Text.replace("error:", "错误:")
    # Text = Text.replace("positional arguments", "参数说明")
    Text = Text.replace("optional arguments", "参数说明")
    Text = Text.replace("unrecognized arguments", "无法识别的参数")
    Text = Text.replace("argument", "参数")
    Text = Text.replace("not allowed with", "(同时只能设置一个源)，后面不允许跟")
    Text = Text.replace("the following arguments are required:",
                        "以下参数是必需的")
    return Text

gettext.gettext = my_i18n

import argparse


if len(sys.argv) == 1:
    sys.argv.append('--help')

parser = argparse.ArgumentParser(

    usage=textwrap.dedent('''\
        ypip [参数] 
        --------------------------------
        例如： 
            ypip -a 设置pip源 为阿里云的
            ypip -q 设置pip源 为清华大学的
           
        '''),
   # description="description啊啊啊", # 参数说明上方， 用法下方
    epilog="如何记忆："
           "参数中的字母都是对应的中文名的第一个拼音,如-a中的a是阿里云拼音(aliyun)的第一个字母,其他类似； "
           "仓库地址：github.cn/xx/ypip",

    # add_help=False
)

group = parser.add_mutually_exclusive_group()
# 外网
group.add_argument('-pypi', action='store_true', help="官方  https://pypi.org/simple/")
group.add_argument('-a', action='store_true', help="阿里云 https://mirrors.aliyun.com/pypi/simple/")
group.add_argument('-q', action='store_true', help="清华大学 https://pypi.tuna.tsinghua.edu.cn/simple")
group.add_argument('-t', action='store_true', help="腾讯 https://mirrors.cloud.tencent.com/pypi/simple")
group.add_argument('-hw', action='store_true', help="华为云 https://mirrors.huaweicloud.com/repository/pypi/simple/")
group.add_argument('-d', action='store_true', help="豆瓣 https://pypi.douban.com/simple/")


# 内网
group.add_argument('-an', action='store_true', help="阿里云内网 https://mirrors.tencentyun.com/pypi/simple")
group.add_argument('-tn', action='store_true', help="腾讯云内网 https://mirrors.aliyuncs.com/pypi/simple/")
group.add_argument('-hwn', action='store_true', help="华为云内网 https://mirrors.myhuaweicloud.com/pypi/web/simple")


args = parser.parse_args()
print("args:",args)
print("args.a:",args.a)
print("args.q:",args.q)
