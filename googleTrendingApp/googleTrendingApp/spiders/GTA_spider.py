from scrapy.spider import Spider
from scrapy.selector import Selector
from googleTrendingApp.items import GoogleTrendingAppItem

class GTASpider(Spider):
	name = "gta"
	allowed_domains = ["play.google.com"]
	start_urls = ["https://play.google.com/store/apps/collection/promotion_300086a_most_popular_multi?hl=en"]

	def parse(self, response):
		sel = Selector(response)
		items = []
		for card in sel.xpath('//div[@class="card-list"]/div[@class="card no-rationale square-cover apps small"]/div'):
			# Made a HUGE mistake here!
			# Only start with //, don't use // in subsequent searches
			name = card.xpath('div[@class="details"]/h2/a/text()').extract()
			company = card.xpath('div[@class="details"]/div[@class="subtitle-container"]/a/text()').extract()
			price = card.xpath('div[@class="details"]/div[@class="subtitle-container"]/span/span/button/span/text()').extract()
			description = card.xpath('div[@class="details"]/div[@class="description"]/text()').extract()
			
			item = GoogleTrendingAppItem()
			item["name"] = name
			item["company"] = company
			item["price"] = price
			item["description"] = description
			items.append(item)
		return items