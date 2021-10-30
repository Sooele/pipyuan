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
            pipyuan -a 设置pip源 为阿里云的
            pipyuan -q 设置pip源 为清华大学的

        '''),
    # description="description啊啊啊", # 用法和参数说明之间
    epilog="如何记忆："
           "参数中的字母都是对应的中文名的第一个拼音,如-a中的a是阿里云拼音(aliyun)的第一个字母,其他类似； "
           "仓库地址：https://github.com/find456789/pipyuan",
)

# subparser_i  = parser.add_subparsers(help=argparse.SUPPRESS) # 用户可能把pipyuan当成pip用，会输入 install
#
# parser_install = subparser_i.add_parser("install")
# parser_install.add_argument("packageName")
parser.add_argument("action", nargs='*', help=argparse.SUPPRESS)  # 隐藏

group = parser.add_mutually_exclusive_group()

# 加载源
for item in yuanList:
    group.add_argument(
        yuanList[item].get("cmd"),
        action='store_true',  # 默认True，支持后面不添加参数
        help=f"{yuanList[item].get('name')} {yuanList[item].get('url')}")

# 自定义源地址
group.add_argument('-zi', metavar='[源地址]', help="自定义源地址（如：pipyuan -zi https://xx.com/simple ）")

args = parser.parse_args()

if args.action:
    if "install" in args.action:
        # 有人 把 pipyuan 当做pip用，打算 pipyuan install xxx
        print("发生错误：你不能把pipyuan 当做pip用，pipyuan只是用来修改源的，不能安装包")
    else:
        print("指令错误！！")
else:
    if args.zi:
        # 我要自定义源地址
        the_url = args.zi
        print(f"你选择了 自定义源:   {the_url} ")
    else:
        my_chose_key = "-" + filter_my_chose(args)
        my_chose_item = yuanList[my_chose_key]
        the_url = my_chose_item.get('url')
        print(f"你选择了:  {my_chose_item.get('name')} {the_url} ")

    cmd_pip_setY: list = cmd_pip + ["config", "set", "global.index-url", the_url]

    set_y = subprocess.call(cmd_pip_setY)

    get_y = subprocess.check_output(cmd_pip_getY)

    print(f"你电脑中 global.index-url 最新值为:{get_y.decode('utf8', 'ignore')}")
