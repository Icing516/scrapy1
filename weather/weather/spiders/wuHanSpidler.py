# -*- coding: utf-8 -*-

import scrapy
from weather.items import WeatherItem

class wuHanSpidler(scrapy.Spider):
    name = 'wuHanSpidler'
    allowed_domains = ["tianqi.com"]
    citys =['wuhan','shanghai']
    start_urls = []
    for city in citys:
        start_urls.append('http://'+city+'.tianqi.com/')

    def parse(self, response):
        subSelecter = response.xpath('//div[@class="tqshow1"]')
        # print subSelecter
        items = []
        for sub in subSelecter:
            item = WeatherItem()
            cityDates = ''
            for cityDate in sub.xpath('./h3//text()').extract():
                cityDates += cityDate
            item['cityDate'] = cityDates
            item['week'] = sub.xpath('./p//text()').extract()[0]
            item['img'] = sub.xpath('./ul/li[1]/img/@src').extract()[0]
            temps = ''
            for temp in sub.xpath('./ul/li[2]//text()').extract():
                temps +=temp
                # print temps
            item['temperature'] = temps
            item['weather'] = sub.xpath('./ul/li[3]//text()').extract()[0]
            item['wind'] = sub.xpath('./ul/li[4]//text()').extract()[0]
            items.append(item)
        return items