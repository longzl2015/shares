# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# 交易日期
# 开盘价
# 收盘价
# 最低价
# 最高价
# 涨跌额
# 涨跌幅(%)
# 成交量(手)
# 成交金额(万元)
# 振幅(%)
# 换手率(%)
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ShareItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()


    opening = scrapy.Field()
    close = scrapy.Field()
    pass
