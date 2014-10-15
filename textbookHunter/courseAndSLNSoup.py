from bs4 import BeautifulSoup
import urllib

rootURL = "http://www.washington.edu/students/timeschd/AUT2014/"

def encodeASCII(text, replacer):
	text = text.encode('ascii', 'replace')
	temp = text.split("???")
	if len(temp) > 1:
		text = temp[0] + replacer + temp[1]
	return text

url = urllib.urlopen(rootURL)
content = url.read()
soup = BeautifulSoup(content)

file = open('CourseAndSLN.txt', 'w')
for tag in soup.find_all("a", "", "href"):
	temp = encodeASCII(tag.get_text(), " ")
	file.write(temp + ": \n")
	url = tag.get("href")
	# if there is an url
	if url is not None:
		# Looks like they only put relative url there
		# So we get rid of those with http
		if ".html" in url and "/" not in url:
			subURL = urllib.urlopen(rootURL + url.strip())
			subContent = subURL.read()
			subSoup = BeautifulSoup(subContent)

			newCourse = False
			firstSLN = False
			for item in subSoup.find_all("a", "", "href"):
				text = item.get_text()
				if any(i.isdigit() for i in text):
					if not all(i.isdigit() for i in text) and ":" not in text:
						if any(i.isdigit() for i in text):
							newCourse = True
							firstSLN = True
							file.write(encodeASCII(text, " ") + "\n")
					else:
						if all(i.isdigit() for i in text) and newCourse:
							file.write(text + "\n")
							newCourse = False


