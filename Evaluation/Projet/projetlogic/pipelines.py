# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymongo

class ProjetlogicPipeline(object):
    def process_item(self, item, spider):
        return item

class MongoPipeline(object):

    collection_name = 'post'

    def open_spider(self, spider):
        self.client = pymongo.MongoClient('localhost',27017)
        self.db = self.client.ouap2018

    def close_spider(self, spider):
        self.client.close()

    def process_item(self, item, spider):
        self.db[self.collection_name].insert_one(dict(item))
        return item