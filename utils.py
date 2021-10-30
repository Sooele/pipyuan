import gettext

# 默认的 argparse 显示的是英文的， 这里覆盖为中文

def my_i18n(Text: str):
    Text = Text.replace("usage", "用法")
    Text = Text.replace("show this help message and exit","查看帮助")
    Text = Text.replace("error:", "错误:")
    # Text = Text.replace("positional arguments", "参数说明")
    Text = Text.replace("optional arguments", "参数说明")
    Text = Text.replace("unrecognized arguments", "无法识别的参数")
    Text = Text.replace("argument", "参数")
    Text = Text.replace("expected one", "需要一个")
    Text = Text.replace("not allowed with", "(同时只能设置一个源)，后面不允许跟")
    Text = Text.replace("the following arguments are required:",
                        "以下参数是必需的")
    return Text

gettext.gettext = my_i18n



def filter_my_chose(args):
    """我选了谁"""
    args_dict = vars(args)
    a1 = dict(filter(lambda e: e[1] is True, args_dict.items())).keys()
    return list(a1)[0]
