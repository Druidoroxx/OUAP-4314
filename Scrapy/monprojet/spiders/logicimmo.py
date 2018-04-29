# -*- coding: utf-8 -*-
import scrapy


class LogicimmoSpider(scrapy.Spider):
    name = 'logicimmo'
    allowed_domains = ['logicimmo.fr']
    start_urls = ['http://logicimmo.fr/']

    def parse(self, response):
        pass
