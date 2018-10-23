# -*- coding: utf-8 -*-
import scrapy
from scrapy import Request
from scrapy.spiders import CrawlSpider, Rule, Spider
from scrapy.linkextractors import LinkExtractor
from lxml import html

_list_of_page = ['https://www.md.com/doctors/allergist-immunologist/florida/~/~',
                  'https://www.md.com/doctors/cardiologist/florida/~/~',
                  'https://www.md.com/doctors/dermatologist/florida/~/~',
                  'https://www.md.com/doctors/ent-otolaryngologist/florida/~/~',
                  'https://www.md.com/doctors/family-doctor/florida/~/~']

class MdSpider(Spider):
    name = 'md'
    allowed_domains = ['md.com']
    start_urls = ['https://www.md.com/doctors/family-doctor/florida/~/~']
    user_agent = "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1"
    meta_proxy = "https://197.149.128.53:49224"
    def start_requests(self):

        for url in self.start_urls:
            yield Request(url)

    def parse(self, response):
        all_urls = response.xpath('//a[@itemprop="url"]/@href').extract()
        doctor_urls = list(set(all_urls))  # make unique
        for doctor in doctor_urls:
            yield Request(doctor, callback=self.parse_deeper)
    #         # yield Request(doctor, self.parse_deeper)
        next_page_url = response.xpath('//li[@class="pagination_next"]//a/@href').extract_first()
        if next_page_url:
            yield Request(next_page_url)

    def parse_deeper(self, response):
        doctor_name = response.xpath('//span[@itemprop="name"]/text()').extract_first()
        speciality = response.xpath('//div[@class="breadcrumbs"]/div[3]/a/span/text()').extract_first()
        first_office = response.xpath('//div[@itemprop="address"]')[0]
        office_name = first_office.xpath('//h3[@itemprop="name"]/text()').extract_first().strip()
        telephone = first_office.xpath('//span[@itemprop="telephone"]/text()').extract_first()
        if telephone:
            pass
        else:
            telephone = "No Phone"
        address = first_office.xpath('//span[@itemprop="streetAddress"]')
        address_1 = address.xpath('//span[@class="street-address-1"]/text()').extract_first()
        address_2 = address.xpath('//span[@class="street-address-2"]/text()').extract_first()
        if address_2:
            final_street_address = address_1 + " " + address_2
        else:
            final_street_address = address_1
        city = first_office.xpath('//span[@itemprop="addressLocality"]/text()').extract_first()
        zip_code = first_office.xpath('//span[@itemprop="postalCode"]/text()').extract_first()
        state = first_office.xpath('//span[@itemprop="addressRegion"]/text()').extract_first()
        yield {
            'Doctor Name' : doctor_name,
            'Speciality' : speciality,
            'Institute' : office_name,
            'Street Address' : final_street_address,
            'City' : city,
            'State' : state,
            'Zip' : zip_code,
            'Phone Number' : telephone,
            'URL': response.url,
        }

#
# from scrapy.crawler import CrawlerProcess
#
# c = CrawlerProcess()
# c.crawl(MdSpider)
# c.start()