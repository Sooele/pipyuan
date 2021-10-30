
# 用途

快速给pip设置源

当我们想给pip设置一个国内源的时候，还要很麻烦的去找源地址

`ypip` （源pip），内置了国内常用的 pip 源， 你可以快速设置想要的源

# 支持的源

- 官方 https://pypi.org/simple/
- 阿里云 https://mirrors.aliyun.com/pypi/simple/
- 清华 https://pypi.tuna.tsinghua.edu.cn/simple
- 腾讯 https://mirrors.cloud.tencent.com/pypi/simple
- 华为 https://mirrors.huaweicloud.com/repository/pypi/simple/
- 豆瓣 https://pypi.douban.com/simple/
- 腾讯内网 https://mirrors.tencentyun.com/pypi/simple
- 阿里内网 https://mirrors.aliyuncs.com/pypi/simple/
- 华为内网 https://mirrors.myhuaweicloud.com/pypi/web/simple

| 指令    | 谁家的  | 源地址                                                     |
|-------|------|---------------------------------------------------------|
| -pypi | 官方   | https://pypi.org/simple/                                |
| -a    | 阿里云  | https://mirrors.aliyun.com/pypi/simple/                 |
| -q    | 清华   | https://pypi.tuna.tsinghua.edu.cn/simple                |
| -t    | 腾讯   | https://mirrors.cloud.tencent.com/pypi/simple           |
| -hw   | 华为   | https://mirrors.huaweicloud.com/repository/pypi/simple/ |
| -d    | 豆瓣   | https://pypi.douban.com/simple/                         |
| -tn   | 腾讯内网 | https://mirrors.tencentyun.com/pypi/simple              |
| -an   | 阿里内网 | https://mirrors.aliyuncs.com/pypi/simple/               |
| -hwn  | 华为内网 | https://mirrors.myhuaweicloud.com/pypi/web/simple       |
| -zi   | ZI   | 自定义源地址（如：ypip -zi https://xx.com/simple ）               |


同样，也可以通过该工具，快速设置你自己的源




# pip config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple
# pip config get global.index-url


