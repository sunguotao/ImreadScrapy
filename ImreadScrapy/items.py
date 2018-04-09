# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ImreadscrapyItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass


class BookItem(scrapy.Item):
    bid = scrapy.Field()
    bDetail = scrapy.Field()
    bImg = scrapy.Field()
    bName = scrapy.Field()
    bAuthor = scrapy.Field()
    #分类
    bClassify = scrapy.Field()
    #标签
    bTag = scrapy.Field()
    #连载/完本
    bState = scrapy.Field()
    #简介
    bIntro = scrapy.Field()

    bSubType = scrapy.Field()
    #字数
    bTextNum = scrapy.Field()