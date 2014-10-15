readFile = open("CourseAndSLN.txt", "r")
writeFile = open("betterCourseAndSLN.txt", "w")
content = readFile.readlines()

for line in content:
	text = line.strip()
	if ":" not in text and not text == "" and "Time Schedule" not in text:
		writeFile.write(text.replace("?", "") + "\n") 