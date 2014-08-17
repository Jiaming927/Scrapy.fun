import urllib, json, csv

leftUrl = 'https://query.yahooapis.com/v1/public/yql?q=select%20*%20from%20yahoo.finance.quotes%20where%20symbol%3D%22'
rightUrl = '%22&format=json&diagnostics=true&env=store%3A%2F%2Fdatatables.org%2Falltableswithkeys&callback='
with open('list.csv', 'rU') as csvFile:
	reader = csv.reader(csvFile)
	for row in reader:
		response = urllib.urlopen(leftUrl + row[1] + rightUrl)
		data = json.loads(response.read())
		with open(row[1] + '.json', 'w') as outfile:
  			json.dump(data['query']['results'], outfile)

# print 'Ask: ' + str(data['query']['results']['quote']['Ask'])
# print 'Change:' + str(data['query']['results']['quote']['Change_PercentChange'])
