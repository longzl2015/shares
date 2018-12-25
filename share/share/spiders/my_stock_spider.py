import scrapy
import re

from share.share.items import ShareItem


class StocksSpider(scrapy.Spider):
    name = 'stocks'
    start_urls = ['http://quote.eastmoney.com/stocklist.html']

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/'
                      '537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safar'
                      'i/537.36',
    }

    def parse(self, response):
        for href in response.css('a::attr(href)').extract():
            try:
                stock = re.findall(r"\d{6}", href)[0]
                url = 'http://quotes.money.163.com/trade/lsjysj_' + stock + '.html'
                yield scrapy.Request(url, headers=self.headers, callback=self.parse_stock)
            except:
                continue

    def parse_stock(self, response):
        for year in response.xpath('//select[@name="year"]/option/text()').extract():
            for season in range(1, 5):
                try:
                    url = response.url + '?year=' + year + '&season=' + season
                    yield scrapy.Request(url, headers=self.headers, callback=self.parse_stock_page)
                except:
                    continue

    def parse_stock_page(self, response):
        response.
        item = ShareItem()







