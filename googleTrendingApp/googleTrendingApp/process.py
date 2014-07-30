import json
from glob import glob

# This code will grab all the items*.json file 
# And do something with it
# Preparing to put this on a server and run this periodically
# Then it can use the data to plot the difference


files = glob('items*.json')

apps = []
for item in files:
	raw = open(item).read()
	data = raw.split('\n')
	for thing in data:
		if (thing != ""):
			obj = json.loads(thing)
			try:
				apps.index(obj['name'])
			except Exception:
				apps.append(obj['name'])
			else:
				print obj['name']