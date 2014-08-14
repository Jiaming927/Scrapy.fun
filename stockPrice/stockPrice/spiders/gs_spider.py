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
		# elt = sel.xpath('//div[@id="price-panel"]/div/span/span/text()')
		# time = elt[1].extract()
		# price = elt[0].extract()

		#//table[@class="snap-data"]/tbody/tr/td[@class="val"]
		elt = sel.xpath('//table[@class="snap-data"]')
		print type(elt)
		# volume = elt[3]
		# Range = elt[0].extract()

		# elt = sel.xpath('//div[@class="id-price-change nwp"]/span/span')
		# change = elt[0].extract()
		# percentage = elt[1].extract()

		# item = StockPriceItem()
		# item["price"] = price
		# item["time"] = time
		# item["volume"] = volume
		# item["Range"] = Range
		# item["change"] = change
		# item["percentage"] = percentage
		# return item

