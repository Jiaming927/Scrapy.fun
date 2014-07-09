import scrapy

class games_spider(scrapy.spider):
  name = games
  allowed_domains = ["sport.williamhill.com"]
  start_url = [
    "http://sports.williamhill.com/bet/en-gb/betting/p/3/tm/World%20Cup%202014/World-Cup-2014.html"
  ]
  
  def parse(self, response):
      filename = response.url.split("/")[-2]
      with open(filename, 'wb') as f:
          f.write(response.body)
