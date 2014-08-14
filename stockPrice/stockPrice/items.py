# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

from scrapy.item import Item, Field

class StockPriceItem(Item):
    price = Field()
    time = Field()
    change = Field()
    percentage = Field()
    Range = Field()
    volume = Field()
    pass
