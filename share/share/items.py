# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# 交易日期
# 开盘价
# 收盘价
# 最低价
# 最高价
# 涨跌额        - AdvanceDecline
# 涨跌幅(%)     - AdvanceDecline
# 成交量(手)     - tradingVolume
# 成交金额(万元) - tradingAmount
# 振幅(%)       - Amplitude
# 换手率(%)     - turnoverRate
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ShareItem(scrapy.Item):
    tradeDate = scrapy.Field()
    openingPrice = scrapy.Field()
    closePrice = scrapy.Field()
    minPrice = scrapy.Field()
    maxPrice = scrapy.Field()
    adAmount = scrapy.Field()
    adRate = scrapy.Field()
    tradingVolume = scrapy.Field()
    tradingAmount = scrapy.Field()
    amplitude = scrapy.Field()
    turnoverRate = scrapy.Field()
    pass
