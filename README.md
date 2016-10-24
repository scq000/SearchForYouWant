#Description
A search tools for downloading based in BT.

#Get Start 使用方法
1. 安装python和pip以及依赖的工具库
   以os x 系统为例
```
brew install python
brew install pip
sudo pip install bs4
sudo pip install requests
```
2. 命令行中使用
```
python search.py keyword
```
keyword为你想要搜索的资源关键字,如果你想多关键字输入，可以使用

```
python search.py 'keyword1 keyword2 ...
```
这种方式

#Pyrailgun 版使用
基于pyrailgun库开发，所以需要
```
sudo pip install pyrailgun
```
由于pyrailgun对于gzip压缩的网页支持不足，所以我更改了其源码，可以在[https://gist.github.com/scq000/d677f0204fc01578df1340a91be1bce1](https://gist.github.com/scq000/d677f0204fc01578df1340a91be1bce1)中获取并替换后使用。

