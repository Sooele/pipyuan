import sys
import textwrap
import subprocess
from utils import gettext, filter_my_chose, setYuan  # gettext 必须在 import argparse 前面，否则翻译不生效
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
        参数列表
            

        '''),
    # description="description啊啊啊", # 用法和参数说明之间
    epilog="如何记忆："
           "参数中的字母都是对应的中文名的第一个拼音,如-a中的a是阿里云拼音(aliyun)的第一个字母,其他类似； "
           "仓库地址：https://github.com/find456789/pipyuan",
)

# 用户可能把pipyuan当成pip用，会输入 install， 用来容错
parser.add_argument("action", nargs='*', help=argparse.SUPPRESS)  # 隐藏

args = parser.parse_args()


if "install" == args.action[0]:
    # 有人 把 pipyuan 当做pip用，打算 pipyuan install xxx
    print("发生错误：你不能把pipyuan 当做pip用，pipyuan只是用来修改源的，不能安装包")
elif "zi" == args.action[0]:
    if len(args.action)==2:
        the_url = args.action[1]
        print(f"你选择了 自定义源:   {the_url} ")
        setYuan(the_url)
    else:
        print("参数错误！参数少了，或者多了，请重新检查")


else:
    if not len(args.action) == 1:
        print("指令错误！！ 正确格式为： pipyuan -a")
    else:
        my_chose_key = yuanList.get(args.action[0])

        try:
            the_url = my_chose_key.get("url")
            print(f"你选择了:  {my_chose_key.get('name')} {the_url} ")
            setYuan(the_url)
        except:
            print("未知指令！ 请检查后再输入")


