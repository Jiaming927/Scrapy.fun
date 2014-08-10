from scrapy.spider import Spider
from scrapy.selector import Selector
from stockPrice.items import StockPriceItem

class GSSpider(Spider):
	name = "googleStock"
	allowed_domains = ["google.com"]
	start_urls = ["https://www.google.com/finance/portfolio?action=view&pid=1&ei=fKXkU_DaG-T2wAO8wIC4BA"]
	print 'hahaha'
	print ''
	def parse(self, response):
		print response
		# sel = Selector(response)
		# items = []
		# for stock in sel.xpath('//tr/td[@class="pf-table-lname pf-table-cell lft"]'):
		# 	name = stock.xpath('a/text()').extract()
		# 	print 'wassup'
		#return items