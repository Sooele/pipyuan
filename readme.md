
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

[comment]: <> (用table是因为网址占用太多空间，指令被迫换行了)
<table>
    <tr>
        <td>指令</td>
        <td>改成谁家的</td>
        <td>助记(拼音)</td>
        <td>源地址</td>
    </tr>
    <tr>
        <td >  <code>pipyuan gf</code> </td>
        <td>官方</td>
        <td> <code>gf </code> 是guanfang的首字母</td>
        <td>https://pypi.org/simple/</td>
    </tr>
    <tr>
        <td> <code>pipyuan a </code> </td>
        <td>阿里云</td>
        <td> <code>a </code> 是aliyun的首字母</td>
        <td>https://mirrors.aliyun.com/pypi/simple/</td>
    </tr>
    <tr>
        <td> <code>pipyuan q </code> </td>
        <td>清华</td>
        <td> <code>q </code> 是qinghua的首字母</td>
        <td>https://pypi.tuna.tsinghua.edu.cn/simple</td>
    </tr>
    <tr>
        <td> <code>pipyuan t </code> </td>
        <td>腾讯</td>
        <td> <code>t </code> 是tengxun的首字母</td>
        <td>https://mirrors.cloud.tencent.com/pypi/simple</td>
    </tr>
    <tr>
        <td> <code>pipyuan h </code> </td>
        <td>华为</td>
        <td> <code>h </code> 是huawei的首字母</td>
        <td>https://mirrors.huaweicloud.com/repository/pypi/simple/</td>
    </tr>
    <tr>
        <td> <code>pipyuan d </code> </td>
        <td>豆瓣</td>
        <td> <code>d </code> 是douban的首字母</td>
        <td>https://pypi.douban.com/simple/</td>
    </tr>
    <tr>
        <td> <code>pipyuan tn </code> </td>
        <td  nowrap="nowrap">腾讯内网</td>
        <td  nowrap="nowrap"> <code>t </code> 是 tengxun 首字母，`n`表示内网</td>
        <td>https://mirrors.tencentyun.com/pypi/simple</td>
    </tr>
    <tr>
        <td> <code>pipyuan an </code> </td>
        <td>阿里内网</td>
        <td> <code>a </code> 是 ali 首字母，`n`表示内网</td>
        <td>https://mirrors.aliyuncs.com/pypi/simple/</td>
    </tr>
    <tr>
        <td> <code>pipyuan hn </code> </td>
        <td>华为内网</td>
        <td> <code>h </code> 是 huawei 首字母，`n`表示内网</td>
        <td>https://mirrors.myhuaweicloud.com/pypi/web/simple</td>
    </tr>
    <tr>
        <td   nowrap="nowrap"> <code>  pipyuan zi url </code> </td>
        <td>自定义</td>
        <td> <code>zi</code> 是 自定义的第一个汉字拼音，不用z是防止未来的冲突</td>
        <td>https://你自己的网址</td>
    </tr>
</table>




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

