# Item: app
# Fields: name, company, price, description
from scrapy.item import Item, Field

class GoogleTrendingAppItem(Item):
    name = Field()
    company = Field()
    price = Field()
    description = Field()
