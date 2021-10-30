import sys
import textwrap
import subprocess
from utils import gettext, filter_my_chose  # gettext 必须在 import argparse 前面，否则翻译不生效
import argparse

from config import yuanList, cmd_pip, cmd_pip_getY

if len(sys.argv) == 1:
    sys.argv.append('--help')

parser = argparse.ArgumentParser(
    usage=textwrap.dedent('''\
        pipyuan [参数] 
        --------------------------------
        例如： 
            pipyuan a 设置pip源 为阿里云的
            pipyuan q 设置pip源 为清华大学的
        --------------------------------
        参数列表
            pypi       官方 https://pypi.org/simple/
            a          阿里云 https://mirrors.aliyun.com/pypi/simple/
            q          清华 https://pypi.tuna.tsinghua.edu.cn/simple
            t          腾讯 https://mirrors.cloud.tencent.com/pypi/simple
            hw         华为 https://mirrors.huaweicloud.com/repository/pypi/simple/
            d          豆瓣 https://pypi.douban.com/simple/
            tn         腾讯内网 https://mirrors.tencentyun.com/pypi/simple
            an         阿里内网 https://mirrors.aliyuncs.com/pypi/simple/
            hwn        华为内网 https://mirrors.myhuaweicloud.com/pypi/web/simple
            zi [源地址]   自定义源地址（如：pipyuan zi https://xx.com/simple ）

           
        '''),
    # description="description啊啊啊", # 用法和参数说明之间
    epilog="如何记忆："
           "参数中的字母都是对应的中文名的第一个拼音,如-a中的a是阿里云拼音(aliyun)的第一个字母,其他类似； "
           "仓库地址：https://github.com/find456789/pipyuan",
# add_help=False

)



parser.add_argument("action",nargs='*', help=argparse.SUPPRESS) #隐藏


parser.print_help()



# 用户可能把pipyuan当成pip用，会输入 install start
# subparser_i  = parser.add_subparsers(help=argparse.SUPPRESS)
# parser_install = subparser_i.add_parser("install")
# parser_install.add_argument("packageName")
# 用户可能把pipyuan当成pip用，会输入 install  end




args = parser.parse_args()

print(args)