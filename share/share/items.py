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
    # 股票名称
    name = scrapy.Field()
    # 股票代码
    code = scrapy.Field()
    # 交易日期
    tradeDate = scrapy.Field()
    # 开盘价
    openingPrice = scrapy.Field()
    # 收盘价
    closePrice = scrapy.Field()
    # 最低价
    minPrice = scrapy.Field()
    # 最高价
    maxPrice = scrapy.Field()
    # 涨跌额
    adAmount = scrapy.Field()
    # 涨跌幅(%)
    adRate = scrapy.Field()
    # 成交量(手)
    tradingVolume = scrapy.Field()
    # 成交金额(万元)
    tradingAmount = scrapy.Field()
    # 振幅(%)
    amplitude = scrapy.Field()
    # 换手率(%)
    turnoverRate = scrapy.Field()
    pass
