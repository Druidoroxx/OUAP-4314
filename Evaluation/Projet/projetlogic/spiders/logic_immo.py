# -*- coding: utf-8 -*-
import scrapy
from scrapy import Request
from ..items import ProjetlogicItem

class LogicImmoSpider(scrapy.Spider):
    name = 'logic_immo'
    allowed_domains = ['logic-immo.com']
    start_urls = ['http://www.logic-immo.com/index-villes-vente.html']
    #Parse la page d'index pour avoir les villes affichées (pas encore toutes les villes, à faire: toutes les autres villes)
    def parse(self, response):
        all_links =[response.urljoin(url) for url in response.css(".logicgrey::attr(href)").extract()]
        for link in all_links:
            yield Request(link,callback=self.parse_cities)
            
    #Parse la première page d'annonce de la ville (à faire : les autres pages)
    def parse_cities(self, response):
        all_links_cities = [response.urljoin(url) for url in response.css(".offer-link::attr(href)").extract()]
        liste_orpi = [response.urljoin(url) for url in response.css(".offer-link::attr(data-orpi)").extract()]
        all_links_cities.extend(liste_orpi)
        all_links_cities = self.clean_orpi(all_links_cities)
        for link in all_links_cities :
            yield Request(link,callback=self.parse_annonce)
            
    #Parse les données nécessaires pour insérer dans MongoDB (pas exactement la structure demandée)
    def parse_annonce(self, response):
        url = response.request.url
        dict_tit = self.title_split(response.css('title::text').extract_first())
        name2 = dict_tit['title']
        desc=response.css('.offer-description-text h2::text').extract_first() + response.css('.offer-description-text p::text').extract_first()
        location = self.clean_spaces(response.css('.offer-block-lastrow p::text').extract_first())
        typ = self.clean_spaces(response.css('.col-xs-3.offer-type p::text').extract_first())
        pr = dict_tit['prix']
        yield ProjetlogicItem(url=url,
                              location=location,
                              name=name2,
                              desc=desc,
                              typ=typ,
                              pr=pr)

    def clean_spaces(self, string_):
        if string_ is not None:
            return " ".join(string_.split())
    
    def clean_orpi(self,liste):
        orpi = "http://www.orpi.com"
        liste= [x for x in liste if x != orpi]
        return liste
    
    def title_split(self,string):
        title,prix = string.split(',')
        prix,c = prix.split('€')
        return {'title':title,'prix':prix}