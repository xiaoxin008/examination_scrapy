# -*- coding: utf-8 -*-

# Define here the models for your scraped items
# 封装返回对象
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class Examination(scrapy.Item):
    # define the fields for your item here like:
    name = scrapy.Field()
    title = scrapy.Field()
    info = scrapy.Field()
