from scrapy import cmdline
cmdline.execute("scrapy runspider my_stock_spider.py -o quotes.json".split())
