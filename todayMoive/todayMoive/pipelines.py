# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

#定义爬取的内容最终怎么处理
class TodaymoivePipeline(object):
    def process_item(self, item, spider):
        return item
