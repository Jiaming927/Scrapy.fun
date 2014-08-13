import csv, os
from scrapy.spider import Spider
from scrapy.selector import Selector
from stockPrice.items import StockPriceItem

class GSSpider(Spider):
	def generateList():
		print os.getcwd()
		result = []
		url = "https://www.google.com/finance?q="
		with open('stockPrice/list.csv', 'rU') as csvFile:
			reader = csv.reader(csvFile)
			for row in reader:
				result.append(url + row[1])
			return result

	name = "googleStock"
	allowed_domains = ["google.com"]
	start_urls = generateList()

	def parse(self, response):
		sel = Selector(response)
		for thing in sel.xpath('//div[@id="price-panel"]/div/span/span/text()'):
			print thing.extract()

