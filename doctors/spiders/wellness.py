# -*- coding: utf-8 -*-
import scrapy


class WellnessSpider(scrapy.Spider):
    name = 'wellness'
    allowed_domains = ['wellness.com']
    start_urls = ['http://wellness.com/']

    def parse(self, response):
        pass
