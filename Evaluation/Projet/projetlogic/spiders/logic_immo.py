# -*- coding: utf-8 -*-
import scrapy
from scrapy import Request
from ..items import ProjetlogicItem

class LogicImmoSpider(scrapy.Spider):
    name = 'logic_immo'
    allowed_domains = ['http://www.logic-immo.com']
    start_urls = ['http://www.logic-immo.com/index-villes-vente.html']

    def parse(self, response):
        all_links =[response.urljoin(url) for url in response.css(".logicgrey::attr(href)").extract()]
        for link in all_links:
            yield Request(link,callback=self.parse_cities)

    def parse_cities(self, response):
        all_links_cities = [response.urljoin(url) for url in response.css(".offer-link::attr(data-orpi)").extract()]
        for link in all_links_cities :
            yield Request(link,callback=self.parse_annonce)
            
    def parse_annonce(self, response):
        lieu = self.clean_spaces(response.css('.offer-block-lastrow p::text').extract_first())
        yield ProjetlogicItem(lieu=lieu)

    def clean_spaces(string_):
        if string_ is not None:
            return " ".join(string_.split())
