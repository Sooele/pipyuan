import sys
import textwrap

from pipyuan import __version__
from pipyuan.utils import gettext, setYuan  # gettext 必须在 import argparse 前面，否则翻译不生效
import argparse

from pipyuan.config import yuanList

if len(sys.argv) == 1:
    sys.argv.append('--help')

def main():
    parser = argparse.ArgumentParser(
        # prog="pipyuan",
        usage=textwrap.dedent('''\
            pipyuan [参数] 
            --------------------------------
            例如： 
                pipyuan a 设置pip源 为阿里云的
                pipyuan q 设置pip源 为清华大学的
            参数列表
                pipyuan gf	官方	https://pypi.org/simple/
                pipyuan a	阿里云	https://mirrors.aliyun.com/pypi/simple/
                pipyuan q	清华	https://pypi.tuna.tsinghua.edu.cn/simple
                pipyuan t	腾讯	https://mirrors.cloud.tencent.com/pypi/simple
                pipyuan h	华为	https://mirrors.huaweicloud.com/repository/pypi/simple/
                pipyuan d	豆瓣	https://pypi.douban.com/simple/
                pipyuan tn	腾讯内网	https://mirrors.tencentyun.com/pypi/simple
                pipyuan an	阿里内网	https://mirrors.aliyuncs.com/pypi/simple/
                pipyuan hn	华为内网	https://mirrors.myhuaweicloud.com/pypi/web/simple
                pipyuan zi [源地址]	自定义	（如：pipyuan zi https://xx.com/simple ）
                
    
            '''),
        # description="description啊啊啊", # 用法和参数说明之间
        # epilog=" 最后的 ",
    )

    # 用户可能把pipyuan当成pip用，会输入 install， 用来容错
    parser.add_argument("action", nargs='*', help=argparse.SUPPRESS)  # 隐藏
    parser.add_argument('-v','--version', action='version', version=f'pipyuan {__version__}', help="查看当前版本号")

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


main()