import csv, os, json
from scrapy.spider import Spider
from scrapy.selector import Selector
from stockPrice.items import StockPriceItem

# Daily email
# Alert email

class GSSpider(Spider):
	def generateList():
		print os.getcwd()
		result = []
		url = "http://finance.yahoo.com/q?s="
		with open('stockPrice/list.csv', 'rU') as csvFile:
			reader = csv.reader(csvFile)
			for row in reader:
				result.append(url + row[1])
			return result

	name = "stockMonitor"
	allowed_domains = ["yahoo.com"]
	start_urls = generateList()
	text = ''

	def alarm(param, limit):

		if (float(param) > limit):
			text += param + ' more than ' + limit + ' \n'
			# Send email

	def parse(self, response):
		sel = Selector(response)
		name = str(sel.xpath('//div[@class="title"]/h2/text()').extract())
		elt = sel.xpath('//div[@class="yfi_rt_quote_summary_rt_top sigfig_promo_1"]/div/span/span/text()')
		time = elt[7].extract()
		price = elt[0].extract()
		change = elt[2].extract()

		alarm(change, 0.05)
		left = name.index('(')
		right = name.index(')')
		name = name[left + 1:right].strip()

		with open('stockPrice/' + name + '.json', 'rU') as jsonFile:
			data = json.load(jsonFile)
			print name
			volumeDif = int(data['quote']['AverageDailyVolume']) - int(data['quote']['Volume'])
			alarm(abs(volumeDif / int(data['quote']['AverageDailyVolume']), 0.05):

			# Set price
			# Lower than YearLow or higher than Yearhigh


		# elt = sel.xpath('//table[@id="table2"]')
		# time = elt[1].extract()
		# price = elt[0].extract()

		#elt = sel.xpath('//table[@class="snap-data"]/tbody/tr/td[@class="val"]')
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

