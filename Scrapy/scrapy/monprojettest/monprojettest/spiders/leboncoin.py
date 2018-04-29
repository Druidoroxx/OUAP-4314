# -*- coding: utf-8 -*-
import scrapy


class LeboncoinSpider(scrapy.Spider):
    name = 'leboncoin'
    allowed_domains = ['leboncoin.fr']
    start_urls = ['http://leboncoin.fr/']

    def parse(self, response):
        pass
