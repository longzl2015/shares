import scrapy


# class MySpider(scrapy.Spider):
    # name = 'mySpider'
    # start_urls = ['http://quotes.money.163.com/trade/lsjysj_603088.html']
    #
    # def parse(self, response):
    #
    #     pass


class QuotesSpider(scrapy.Spider):

    name = "quotes"
    start_urls = [
        'http://quotes.toscrape.com/tag/humor/',
    ]

    def parse(self, response):
        for quote in response.css('div.quote'):
            yield {
                'text': quote.css('span.text::text').extract_first(),
                'author': quote.xpath('span/small/text()').extract_first(),
            }

        next_page = response.css('li.next a::attr("href")').extract_first()
        if next_page is not None:
            yield response.follow(next_page, self.parse)

