# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

from scrapy import signals
from scrapy.contrib.exporter import CsvItemExporter


class SpiderPipeline(CsvItemExporter):

    def __init__(self):
        self.files = {}

    @classmethod
    def from_crawler(cls, crawler):
        print('==========pipeline==========from_crawler==========')
        pipeline = cls()
        crawler.signals.connect(pipeline.spider_opened, signals.spider_opened)
        crawler.signals.connect(pipeline.spider_closed, signals.spider_closed)
        return pipeline

    def spider_opened(self, spider):
        save_file = open('share_export.csv', 'wb+')
        self.files[spider] = save_file
        self.exporter = CsvItemExporter(save_file)
        self.exporter.start_exporting()

    def spider_closed(self, spider):
        self.exporter.finish_exporting()
        save_file = self.files.pop(spider)
        save_file.close()

    def process_item(self, item, spider):
        print(type(item))
        self.exporter.export_item(item)
        return item
