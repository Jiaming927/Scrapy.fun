import json
import sys
import string
import plotly.plotly as py
from plotly.graph_objs import *
from glob import glob

# This code will grab all the items*.json file 
# And do something with it
# Preparing to put this on a server and run this periodically
# Then it can use the data to plot the difference

py.sign_in('Python-Demo-Account', 'gwt101uhh0')
files = glob('items*.json')
filesNum = len(files)
print files

apps = {}
dataXList = []
dataYList = []
for item in files:
	raw = open(item).read()
	data = raw.split('\n')
	for thing in data:
		if (thing != ""):
			obj = json.loads(thing)
			name = string.strip(obj['name'][0])
			if name in apps:
				apps[name] = apps[name] + 1
			else:
				apps[name] = 1

if len(sys.argv) < 2:
	for key in apps:
		print key.encode('utf-8').strip() + ' has been in trending apps ' + str(apps[key]) + ' time(s).'
	# 	dataXList.append(key)
	# 	dataYList.append(apps[key])

	# data = Data([
	#     Bar(
	#         x=dataXList,
	#         y=dataYList
	#     )
	# ])

	# plot_url = py.plot(data, filename='basic-bar')
else:
	param = sys.argv[1]

	if param == 'always':
		for key in apps:
			if (apps[key] == filesNum):
				print key.encode('utf-8').strip()
	
	else:
		name = param
		if name not in apps:
			print 'name not in apps'
		else:
			dataXList.append(name)
			dataYList.append(apps[name])
			data = Data([
			    Bar(
			        x=dataXList,
			        y=dataYList
			    )
			])
			plot_url = py.plot(data, filename='basic-bar')


# try:
# 	apps.index(obj['name'])
# except Exception:
# 	apps.append(obj['name'])
# else:
# 	print obj['name']