from bs4 import BeautifulSoup
import urllib

url = urllib.urlopen("http://sports.williamhill.com/bet/en-gb/betting/")

content = url.read()

soup = BeautifulSoup(content)

for a in soup.find_all("a", {"class" : "h"}):
	if a.parent.name == "td":
		print a["title"].encode('GBK') 

for li in soup.find_all("li", {"class" : "home betli"}):
	print li.getText();

for li in soup.find_all("li", {"class" : "deuce betli"}):
	print li.getText();

for li in soup.find_all("li", {"class" : "visit betli exp"}):
	print li.getText();


