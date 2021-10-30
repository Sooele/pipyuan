import gettext

# 默认的 argparse 显示的是英文的， 这里覆盖为中文
import subprocess

from pipyuan.config import cmd_pip_getY, cmd_pip


def my_i18n(Text: str):
    Text = Text.replace("usage", "用法")
    Text = Text.replace("show this help message and exit","查看帮助")
    Text = Text.replace("error:", "错误:")
    # Text = Text.replace("positional arguments", "参数说明")
    Text = Text.replace("optional arguments", "其他参数")
    Text = Text.replace("unrecognized arguments", "无法识别的参数")
    Text = Text.replace("argument", "参数")
    Text = Text.replace("expected one", "需要一个")
    Text = Text.replace("not allowed with", "(同时只能设置一个源)，后面不允许跟")
    Text = Text.replace("the following arguments are required:",
                        "以下参数是必需的")
    return Text

gettext.gettext = my_i18n



def setYuan(the_url):
    cmd_pip_setY: list = cmd_pip + ["config", "set", "global.index-url", the_url]

    set_y = subprocess.call(cmd_pip_setY)

    get_y = subprocess.check_output(cmd_pip_getY)

    print(f"你电脑中 global.index-url 最新值为:{get_y.decode('utf8', 'ignore')}")
