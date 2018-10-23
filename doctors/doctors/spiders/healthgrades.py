# -*- coding: utf-8 -*-
import scrapy


class HealthgradesSpider(scrapy.Spider):
    name = 'healthgrades'
    allowed_domains = ['healthgrades.com']
    start_urls = ['http://healthgrades.com/']

    def parse(self, response):
        pass
