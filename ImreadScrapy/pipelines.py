# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymongo
from scrapy.conf import settings
from .items import BookItem


class ImreadscrapyPipeline(object):
    def __init__(self):
        connection = pymongo.MongoClient(settings['MONGODB_HOST'], settings['MONGODB_PORT'])
        self.db = connection[settings['MONGODB_NAME']]

    def process_item(self, item, spider):
        _ = spider
        if isinstance(item,BookItem):
            post = self.db[settings['MONGODB_QIANDIANNAME']]
            post.update({'bid': item['bid']}, {'$set': dict(item)}, upsert=True)
            print('sun','数据库更新成功')
        return item
