# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ProjetlogicItem(scrapy.Item):
    url = scrapy.Field()
    location = scrapy.Field()
    name = scrapy.Field()
    desc = scrapy.Field()
    typ = scrapy.Field()
    pr = scrapy.Field()
