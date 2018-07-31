# -*- coding: utf-8 -*-
import pymongo

from douban.settings import mongo_host,mongo_port,mongo_db_collection,mongo_db_name

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
#引入pymongo


class DoubanPipeline(object):

    #初始化Mongodb的数据库
    def __init__(self):
        # print ("-----------"+mongo_host)
        host = mongo_host
        port = mongo_port
        dbname = mongo_db_name
        sheetname = mongo_db_collection
        click = pymongo.MongoClient(host=host,port=port)
        mydb = click[dbname]
        self.post = mydb[sheetname]

    #解析数据并存储到Mongodb
    def process_item(self, item, spider):
        data = dict(item)
        self.post.insert(data)
        return item
