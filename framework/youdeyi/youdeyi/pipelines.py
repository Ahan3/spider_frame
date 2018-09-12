# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json
from pymongo import MongoClient

class YoudeyiPipeline(object):

    def open_spider(self,spider):
        if spider.name == "39":
            self.f = open('info.jsonlines','w',encoding='utf-8')

    def process_item(self, item, spider):
        if spider.name == "39":
            json.dump(dict(item),self.f,ensure_ascii=False)
            self.f.write('\n')
        return item

    def spider_close(self,spider):
        if spider.name == "39":
            self.f.close()

class MongodbPipeline(object):
    def open_spider(self,spider):
        client = MongoClient('localhost',27017)
        self.db = client['youdeyi']['askDocker39']

    def process_item(self,item,spider):
        if spider.name == '39':
            self.db.insert(dict(item))
        return item

    def close_spider(self,spider):

        if spider.name == '39':
            self.db.close()