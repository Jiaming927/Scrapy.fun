from bs4 import BeautifulSoup
import urllib

url = urllib.urlopen("http://c.caipiao.taobao.com/lottery/order/lottery_jczq_hhgg_by_client.htm")

content = url.read()

soup = BeautifulSoup(content)

# td .Home team => a .h => title


for a in soup.find_all("a", {"class" : "h"}):
	if a.parent.name == "td":
		print a["title"].encode('GBK') 

for li in soup.find_all("li", {"class" : "home betli"}):
	print li.getText();

for li in soup.find_all("li", {"class" : "deuce betli"}):
	print li.getText();

for li in soup.find_all("li", {"class" : "visit betli exp"}):
	print li.getText();

home = {"win": , "draw": , "lose":}

visit = {"win": , "draw": , "lose":}

result = []

for homeKey in home:
	for visitKey in visit
		print homeKey + " " + visitKey + ":" home[homeKey] * visit[visitKey]


