

方便好记， 单词 `pipyuan` 由 `pip` 和 `yuan` 组成； 助记： pip源


# 用途

快速给 pip 设置源

当我们想给 pip 设置一个国内源的时候，还要很麻烦的去找源地址

`pipyuan` 内置了国内常用的 pip 源， 你可以快速设置想要的源

# 支持的源
 
| 谁家的    | 源地址                                                     | 指令                | 助记            |
|--------|---------------------------------------------------------|-------------------|---------------|
| 官方     | https://pypi.org/simple/                                | `pipyuan -gf`     | 官方 拼音(GuanFang) 首字母     |
| 阿里云    | https://mirrors.aliyun.com/pypi/simple/                 | `pipyuan -a`      | aliyun的第一个字母a  |
| 清华     | https://pypi.tuna.tsinghua.edu.cn/simple                | `pipyuan -q`      | qinghua的第一个字母q |
| 腾讯     | https://mirrors.cloud.tencent.com/pypi/simple           | `pipyuan -t`      | tengxun的第一个字母t |
| 华为     | https://mirrors.huaweicloud.com/repository/pypi/simple/ | `pipyuan -hw`     | Hua Wei的缩写hw     |
| 豆瓣     | https://pypi.douban.com/simple/                         | `pipyuan -d`      | douban的第一个字母d  |
| 腾讯内网   | https://mirrors.tencentyun.com/pypi/simple              | `pipyuan -tn`     | 腾(t)讯内(n)网 拼音 首字母               |
| 阿里内网   | https://mirrors.aliyuncs.com/pypi/simple/               | `pipyuan -an`     |    阿(a)里内(n)网    拼音 首字母        |
| 华为内网   | https://mirrors.myhuaweicloud.com/pypi/web/simple       | `pipyuan -hwn`    |    华(h)为(w)内(n)网   拼音 首字母        |
| 自定义源地址 | （如：pipyuan -zi https://xx.com/simple ）                  | `pipyuan -zi url` |  自己 > 自 > zi         |



# pipyuan有啥好处

- 方便好记， `pipyuan` 由 pip 和 yuan 组成；助记： pip源
- 很轻巧，不依赖其他第三方包，只依赖Python自带的包


# 平时怎么用

假设你在一个新电脑上。刚安装了python，那么接下来你只需要：

1. 安装pipyuan：
   - `python -m pip install pipyuan` 或者 `pip install pipyuan `
2. 使用pip源修改本地的源
   - `pipyuan -a`  比如修改为阿里云的源
   
3. 愉快的使用 pip 安装其他包（这时候你的源已经被修改好了


# 欢迎提供建议

有啥建议，请给我提出，谢谢


[comment]: <> (# pip config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple)

[comment]: <> (# pip config get global.index-url)


