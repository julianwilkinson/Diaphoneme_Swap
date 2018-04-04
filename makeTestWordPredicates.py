import os

sourceFileName = input("Enter the source file name: ")
while True:
	try:
		source = open(sourceFileName, 'r', encoding='utf-8')
		print("File Opened Successfully")
		break
	except IOError:
		print("Could not open file")

destinationFileName, extension = os.path.splitext(sourceFileName)
destinationFileName +=".swipl"
while True:
	try:
		destination = open(destinationFileName, 'w', encoding="utf-8")
		print("File Created Successfully")
		break
	except IOError:
		print("Unable to make file")
		sys.exit()

next(source) #skip first line and BOM
for line in source:
	word = line.split()
	if len(word) == 1:
		output = "testWord(["
		cluster = ""
		clusterFlag = False
		for char in word[0]:
			if char == "(":
				clusterFlag = True
				cluster += "["
			elif char == ")":
				cluster = cluster[:-1]
				cluster += "],"
				clusterFlag = False
				output += cluster
				cluster = ""
			elif clusterFlag:
				cluster += "['"+ char + "'],"
			else:
				output += "['" + char + "'],"
		output = output[:-1]
		output += "]). %" + word[0] + " \n"

		destination.write(output)

destination.close()
