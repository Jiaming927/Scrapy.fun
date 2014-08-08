from scrapy.spider import Spider
from scrapy.selector import Selector
from stockPrice.items import StockPriceItem

class GTASpider(Spider):
	name = "googleStock"
	allowed_domains = ["google.com"]
	start_urls = ["https://www.google.com/finance/portfolio?action=view&pid=1&ei=fKXkU_DaG-T2wAO8wIC4BA"]

	def parse(self, response):
		
		return items