# -*- coding: utf-8 -*-
import scrapy


class MdSpider(scrapy.Spider):
    name = 'md'
    allowed_domains = ['md.com']
    start_urls = ['https://www.md.com/doctors/cardiologist/florida/~/~']
    def start_requests(self):
        # all urls here 
        pass

    def parse(self, response):
        pass
