from bs4 import BeautifulSoup
import urllib

url = urllib.urlopen("http://c.caipiao.taobao.com/lottery/order/lottery_jczq_hhgg_by_client.htm?spm=a2126.6843133.1151804389.d4912993.YJTbx5")

content = url.read()

soup = BeautifulSoup(content)

for td in soup.find_all("td"):
	print td