import json
from glob import glob

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