# -*- coding: utf-8 -*-

import scrapy
from todayMoive.items import TodaymoiveItem
import json

class moiveSpidler(scrapy.Spider):
    name = 'moiveSpidler'
    allowed_domains = ["www.jycinema.com"]
    # start_urls = ('http://www.jycinema.com/frontUIWebapp/appserver/cinCinemaFilmViewService/findFilm',)
    headers = {'Host': 'www.jycinema.com',
            'Content-Type': 'application/json',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36'}
    # meta = {'params': '{"type":"queryFilm","cityName":"深圳市","cinemaId":"","statusRE":"RELEASE","channelCode":"J0002","channelId":"3"}'}

    def start_requests(self):
        url = 'http://www.jycinema.com/frontUIWebapp/appserver/cinCinemaFilmViewService/findFilm'
        form_data = {
            'params': '''{"type":"queryFilm","cityName":"深圳市","cinemaId":"","statusRE":"RELEASE","channelCode":"J0002","channelId":"3"}'''
        }
        return [scrapy.FormRequest(url, formdata=form_data,headers=self.headers,callback=self.parse_item)]

    def parse_item(self, response):
        sel = json.loads(response.body_as_unicode())
        film1 = sel['data']
        items = []
        for film in film1:
            item =TodaymoiveItem()
            item['moiveName']=film['filmName']
            # print film['filmName']
            items.append(item)
        return items




