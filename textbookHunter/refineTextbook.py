readFile = open("Textbook.txt", "r")
writeFile = open("*Textbookfile.txt", "w")
content = readFile.readlines()

prevBook = ""

i = 0

while i < len(content):
	if content[i] != prevBook:
		prevBook = content[i]
		writeFile.write('*' + prevBook)

	writeFile.write(content[i + 1].strip() + "\n")
	writeFile.write(content[i + 2].strip() + "\n")
	writeFile.write(content[i + 3].replace("*", ""))
	i += 4


