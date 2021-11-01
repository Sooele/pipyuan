
![PyPI](https://img.shields.io/pypi/v/pipyuan)
![PyPI - Python Version](https://img.shields.io/pypi/pyversions/pipyuan)
![PyPI - Wheel](https://img.shields.io/pypi/wheel/pipyuan)


方便好记， 单词 `pipyuan` 由 `pip` 和 `yuan` 组成； 助记： pip源

# 项目地址：
https://github.com/find456789/pipyuan

# 用途

快速给 pip 设置源

当我们想给 pip 设置一个国内源的时候，还要很麻烦的去找源地址

`pipyuan` 内置了国内常用的 pip 源， 你可以快速设置想要的源

# 使用

假设你在一个新电脑上。刚安装了python，那么接下来你只需要：

1. 安装 pipyuan：
   - `python -m pip install pipyuan` 或者 `pip install pipyuan `
2. 使用 pipyuan 修改本地的源
   - `pipyuan a`  修改为阿里云的源
   
3. 愉快的使用 pip 安装其他包（这时候你的源已经被修改好了）



# 支持的源
 
| 源地址                                                     | 谁家的    | 指令               | 助记                   |
|---------------------------------------------------------|--------|------------------|----------------------|
| https://pypi.org/simple/                                | 官方     | `pipyuan gf`     | `gf`是guanfang的首字母（官方）  |
| https://mirrors.aliyun.com/pypi/simple/                 | 阿里云    | `pipyuan a`      | `a`是aliyun的首字母        |
| https://pypi.tuna.tsinghua.edu.cn/simple                | 清华     | `pipyuan q`      | `q`是qinghua的首字母      |
| https://mirrors.cloud.tencent.com/pypi/simple           | 腾讯     | `pipyuan t`      | `t`是tengxun的首字母       |
| https://mirrors.huaweicloud.com/repository/pypi/simple/ | 华为     | `pipyuan h`      | `h`是huawei的首字母        |
| https://pypi.douban.com/simple/                         | 豆瓣     | `pipyuan d`      | `d`是douban的首字母        |
| https://mirrors.tencentyun.com/pypi/simple              | 腾讯内网   | `pipyuan tn`     | `t`是 tengxun 首字母，`n`表示内网   |
| https://mirrors.aliyuncs.com/pypi/simple/               | 阿里内网   | `pipyuan an`     | `a`是 ali 首字母，`n`表示内网   |
| https://mirrors.myhuaweicloud.com/pypi/web/simple       | 华为内网   | `pipyuan hn`     | `h`是 huawei 首字母，`n`表示内网    |
| https://xx.cn/simple                    | 自定义源地址 | `pipyuan zi url` | `zi` 是 自定义的第一个汉字拼音，不用z是防止未来的冲突        |



# `pipyuan` 后面的字母参数是什么意思？

答：是对应公司的拼音的首字母

比如：`pipyuan a`
这里面的 `a` ， 就是 **a**liyun(阿里云的拼音) ->  拼音的第一个字母就是a

再比如：`pipyuan q`
这里面的 `q` ， 就是 **q**inghuadaxue(清华大学的拼音) -> 拼音的第一个字母就是q

----

再举例：

我想改成 `豆瓣` 的源， 拼音 `douban` 的第一个字母是 `d `， 那我就执行 `pipyuan d`

我想改成 `腾讯` 的源， 拼音 `tengxun` 的第一个字母是 `t `， 那我就执行 `pipyuan t`




# `pipyuan` 很轻巧

- 方便好记， `pipyuan` 由 `pip` 和 `yuan` 组成；助记： pip源
- 很轻巧，不依赖其他第三方包，只依赖Python自带的包

# `pipyuan` 内部的原理是什么？

内部调用了 `python -m pip config set global.index-url [源地址]` 来修改源

所以，需要确保你电脑里的 `python` 指向了正确的位置

[comment]: <> (# `pipyuan` 高级命令)

[comment]: <> (待添加。。。 )


# 欢迎提供建议

有啥建议，请给我提出，谢谢


[comment]: <> (打包 https://packaging.python.org/tutorials/packaging-projects/)

[comment]: <> (# pip config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple)
[comment]: <> (# python -m pip config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple)

[comment]: <> (# pip config get global.index-url)

[comment]: <> (# 待添加的功能 )

[comment]: <> ([ ] 目前是直接替换为某个源，未来支持 在原基础上 新增源（有时候想同时用多个源）)

[comment]: <> (   pipyuan jia a, 在原基础上，增加 阿里云)

[comment]: <> (   pipyuan jiazi 在源基础上，增加 自定义的源)

[comment]: <> (   pipyuan a 把现有的所有的，替换为 阿里云的)

