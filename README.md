python 2.7

安装pip

pip install scrapy

scrapy 查看是否完成

scrapy 框架

￼

scrapy engine 
scheduler 请求队列
downloader 下载
spiders 数据解析 
itempipeline 数据处理、过滤、存储

新建项目 scrapy startproject douban

在spiders目录下生成正则表达式 等文件,创建命令为：
scrapy genspider douban_spider movie.douban.com

在项目的目录下输入 启动
scrapy crawl douban_spider

在spider中解析数据

保存 csv 和 json数据
scrapy crawl douban_spider -o a.json

shiyong mongdb


docker run --name cool-mongo -p 27017:27017 -d mongo 

