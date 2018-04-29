# -*- coding: utf-8 -*-
import scrapy


class LogicImmoSpider(scrapy.Spider):
    name = 'logic-immo'
    allowed_domains = ['www.logic-immo.com/']
    start_urls = ['http://www.logic-immo.com//']

    def parse(self, response):
        pass
