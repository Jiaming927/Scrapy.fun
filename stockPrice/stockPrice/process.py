import urllib, json, csv

def getData(stock):
	url = 'https://query.yahooapis.com/v1/public/yql?q=select%20*%20from%20yahoo.finance.quotes%20where%20symbol%3D%22' + stock + '%22&format=json&diagnostics=true&env=store%3A%2F%2Fdatatables.org%2Falltableswithkeys&callback='
	response = urllib.urlopen(url);
	data = json.loads(response.read())
	print 'Ask: ' + str(data['query']['results']['quote']['Ask'])
	print 'Change:' + str(data['query']['results']['quote']['Change_PercentChange'])


with open('list.csv', 'rU') as csvFile:
	reader = csv.reader(csvFile)
	for row in reader:
		print 'Getting ' + row[0]
		getData(row[1])