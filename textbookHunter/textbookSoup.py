from bs4 import BeautifulSoup
import urllib

rootURL = "http://sdb.admin.washington.edu/textbooks/query.asp?qtr=Autumn&sln1="

def encodeASCII(text, replacer):
	text = text.encode("ascii", "replace")
	temp = text.split("?")
	if len(temp) > 1:
		text = temp[0] + replacer + temp[1]
	return text

readFile = open("betterCourseAndSLN.txt", "r")
writeFile = open("Textbook.txt", "w")
content = readFile.readlines()
course = ""

for line in content:
	if line.strip().isdigit():
		SLN = line.strip()
		# UNCOMMENT THIS TO DEBUG OR SEE PROGRESS
		#print SLN
		url = urllib.urlopen(rootURL + str(SLN))
		content = url.read()
		soup = BeautifulSoup(content)
		thing = soup.find_all("td")
		# for td in soup.find_all("tr", "", "td"):
		# for i in range(len(thing)):
		#   	print i
		#   	print thing[i]
		# 	# if len(td.attrs) == 0:
		# 	# 	print td
		if not thing[13].getText().startswith("No"):
			index = 14
			while not "not required" in thing[index].getText() and not thing[index].getText().startswith(" *Some") and not thing[index].getText().strip() == "":
				writeFile.write(course + "\n")
				writeFile.write("Name: " + encodeASCII(thing[index].getText(), " ") + "\n")
				writeFile.write("Author: " + encodeASCII(thing[index + 1].getText(), " ") + "\n")
				writeFile.write("Price: " + encodeASCII(thing[index + 2].getText(), " ") + "\n")
				index += 7
	else:
		course = line.strip()

