import scrapy
import urllib
from bs4 import BeautifulSoup

class games_spider(scrapy.spider):
  name = games
  allowed_domains = ["sport.williamhill.com"]
  start_url = [
    "http://sports.williamhill.com/bet/en-gb/betting/p/3/tm/World%20Cup%202014/World-Cup-2014.html"
  ]
  
  def parse(self, response):
    content = response.body
    soup = BeautifulSoup(content)
    for tbody in soup.find_all("tbody"):
      print tbody.getText()
      div => tbody
      table => thead => tr => th => span
      table => tbody => tr => td => div
