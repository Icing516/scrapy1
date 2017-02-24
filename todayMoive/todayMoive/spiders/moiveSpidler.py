# -*- coding: utf-8 -*-

import scrapy
from todayMoive.items import TodaymoiveItem
from scrapy.spiders import CrawlSpider
from scrapy.http import Request
from scrapy.selector import Selector
from scrapy.http import Request, FormRequest
import json

class moiveSpidler(CrawlSpider):
    name = 'moiveSpidler'
    allowed_domains = ["www.jycinema.com"]
    start_urls = ('http://www.jycinema.com/frontUIWebapp/appserver/cinCinemaFilmViewService/findFilm')
    headers = {'Host': 'www.jycinema.com',
            'Content-Type': 'application/x-www-form-urlencoded;charset=UTF-8',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36'}

    # def start_requests(self):
    #     return Request(self.start_urls,
    #                     headers=self.headers,
    #                     meta ={'params': '''{"type":"queryFilm","cityName":"深圳市","cinemaId":"","statusRE":"RELEASE","channelCode":"J0002","channelId":"3"}'''},
    #                     callback=self.parse)


    def start_requests(self):
        print '开始爬虫。。。'
        # param = {'params': '''{"type":"queryFilm","cityName":"深圳市","cinemaId":"","statusRE":"RELEASE","channelCode":"J0002","channelId":"3"}'''}
        return [FormRequest(url=self.start_urls,  # "http://www.zhihu.com/login",
                            # meta={'cookiejar': response.meta['cookiejar']},
                            headers=self.headers,  # 注意此处的headers
                            formdata={'params':'{"type":"queryFilm","cityName":"深圳市","cinemaId":"","statusRE":"RELEASE","channelCode":"J0002","channelId":"3"}'},
                            callback=self.parse,
                            )]

    def parse(self, response):
        print 'response=',response
        subSelecter = Selector(response)
        # subSelecter = response.content
        print '获取电影数据。。。'
        print subSelecter
        items =[]
        json_result = json.loads(subSelecter)
        items = json_result['data']

        for item in items:
            item = TodaymoiveItem()
            item['moiveName'] = str(item['filmName'])
            items.append(item)
            print item['filmName']

        # for sub in subSelecter:
        #     item = TodaymoiveItem()
        #     item['moiveName'] = sub.xpath('').extract()
        #     items.append(item)
        return items