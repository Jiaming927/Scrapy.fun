from bs4 import BeautifulSoup
import urllib

url = urllib.urlopen("http://c.caipiao.taobao.com/lottery/order/lottery_jczq_hhgg_by_client.htm?spm=a2126.6843133.1151804389.d4912993.YJTbx5")

content = url.read()

# soup = BeautifulSoup(content, fromEncoding=”GB18030“)
soup = BeautifulSoup(content);

# Home team
# Visit team


for li in soup.originalEncoding.find_all("li", {"class" : "home betli"}):
	print li.getText();

for li in soup.originalEncoding.find_all("li", {"class" : "deuce betli"}):
	print li.getText();

for li in soup.originalEncoding.find_all("li", {"class" : "visit betli exp"}):
	print li.getText();