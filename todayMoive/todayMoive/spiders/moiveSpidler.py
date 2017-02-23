# -*- coding: utf-8 -*-

import scrapy
from todayMoive.items import TodaymoiveItem
from scrapy.spiders import CrawlSpider
from scrapy.http import Request
from scrapy.selector import Selector

class moiveSpidler(CrawlSpider):
    name = 'moiveSpidler'
    allowed_domains = ["jycinema,com"]
    start_urls = ('http://www.jycinema.com/frontUIWebapp/appserver/cinCinemaFilmViewService/findFilm',)
    head = {'Host': 'www.jycinema.com',
            'Content-Type': 'application/x-www-form-urlencoded;charset=UTF-8',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36'}

    param = {
        'params': '''{"type":"queryFilm","cityName":"深圳市","cinemaId":"","statusRE":"RELEASE","channelCode":"J0002","channelId":"3"}'''}

    def parse(self, response):
        subSelecter = response.content
        print subSelecter
        items =[]
        for sub in subSelecter:
            item = TodaymoiveItem()
            item['moiveName'] = sub.xpath('').extract()
            items.append(item)
        return items