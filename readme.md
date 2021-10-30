
# 用途

快速给pip设置源

当我们想给pip设置一个国内源的时候，还要很麻烦的去找源地址

`ypip` （源pip），内置了国内常用的 pip 源， 你可以快速设置想要的源

# 支持的源
 

| 指令    | 谁家的  | 源地址                                                     |
|-------|------|---------------------------------------------------------|
| ypip -pypi | 官方   | https://pypi.org/simple/                                |
| ypip -a    | 阿里云  | https://mirrors.aliyun.com/pypi/simple/                 |
| ypip -q    | 清华   | https://pypi.tuna.tsinghua.edu.cn/simple                |
| ypip -t    | 腾讯   | https://mirrors.cloud.tencent.com/pypi/simple           |
| ypip -hw   | 华为   | https://mirrors.huaweicloud.com/repository/pypi/simple/ |
| ypip -d    | 豆瓣   | https://pypi.douban.com/simple/                         |
| ypip -tn   | 腾讯内网 | https://mirrors.tencentyun.com/pypi/simple              |
| ypip -an   | 阿里内网 | https://mirrors.aliyuncs.com/pypi/simple/               |
| ypip -hwn  | 华为内网 | https://mirrors.myhuaweicloud.com/pypi/web/simple       |
| ypip -zi url  | 自定义源地址   | （如：ypip -zi https://xx.com/simple ）               |


# ypip有啥好处

- 方便好记， `ypip` 是一个可以快速更换源的pip,字母y就是源的拼音(yuan)的第一个字母






[comment]: <> (# pip config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple)

[comment]: <> (# pip config get global.index-url)


