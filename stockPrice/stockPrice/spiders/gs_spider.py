from scrapy.spider import Spider
from scrapy.selector import Selector
from stockPrice.items import StockPriceItem

class GSSpider(Spider):
	name = "googleStock"
	allowed_domains = ["google.com"]
	start_urls = [""]
	def parse(self, response):