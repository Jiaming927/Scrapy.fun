import json
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

for key in apps:
	dataXList.append(key)
	dataYList.append(apps[key])

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