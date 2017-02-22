# -*- coding: utf-8 -*-

import scrapy

class moiveSpidler(scrapy.Spider):
    name = 'moiveSpidler'
    allowed_domains = ["jycinema,com"]
    start_urls = ('http://www.jycinema,com',)

    def parse(self, response):
        pass