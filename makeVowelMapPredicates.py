import os

wellsFileName = "wells_index.txt"
with open("Dialects/" + wellsFileName, 'r') as dialect1_File:
	destinationFileName = "dialects.swipl"
	while True:
		try:
			destination = open(destinationFileName, 'w', encoding="utf-8")
			print(destinationFileName + " Created Successfully")
			break
		except IOError:
			print("Unable to make " + destinationFileName)
			print("Quitting...")
			sys.exit()
	dialectNamePredicateList = []
	for file in os.listdir("Dialects"):
		if file.endswith(".txt") and (file is not "wells_index.txt"):
			while True:
				try:
					dialect0_File = open("Dialects/" + file, 'r')
					print(file + " Opened Successfully")
					break
				except IOError:
					print("Could not open " + file)
					print("Quitting...")
					sys.exit()


			next(dialect0_File) #skip first line and BOM
			next(dialect1_File) #skip first line and BOM

			dialect0, extension = os.path.splitext(file)
			dialect1, extension = os.path.splitext(wellsFileName)


			destination.write("%  " + str(dialect0) + "\n")

			#Store list of dialect predicates to write out later
			dialectNamePredicateList.append("dialect('" + str(dialect0) + "').\n")

			for dialect0Line, dialect1Line  in zip(dialect0_File,dialect1_File):
				for dialect0Map in dialect0Line.split():
					dialect0_toAdd = ""
					if len(dialect0Map) > 1:
						for char in dialect0Map:
							# dialect0_toAdd += "['\\x" + str(hex(ord(char)))[2:] + "'],"
							dialect0_toAdd += "['" + char + "'],"
						dialect0_toAdd = dialect0_toAdd[:-1] #remove last comma
					else:
						# dialect0_toAdd = "'\\x" + str(hex(ord(dialect0Map)))[2:] + "'"
						dialect0_toAdd = "'" + dialect0Map + "'"

					for dialect1Map in dialect1Line.split():
						dialect1_toAdd = ""
						if len(dialect1Map) > 1:
							for char in dialect1Map:
								# dialect1_toAdd += "['\\x" + str(hex(ord(char)))[2:] + "'],"
								dialect1_toAdd += "['" + char + "'],"
							dialect1_toAdd = dialect1_toAdd[:-1] #remove last comma
						else:
							# dialect1_toAdd = "'\\x" + str(hex(ord(dialect1Map)))[2:] + "'"
							dialect1_toAdd = "'" + dialect1Map + "'"

						destination.write("diaphoneme([" + str(dialect0_toAdd) + "],['" + str(dialect0) + "'],[" + str(dialect1_toAdd) + "],['" + str(dialect1) + "']).\n")
			dialect1_File.seek(0, 0)
			destination.write("\n\n\n")

	destination.write("% dialects\n")
	for dialect in dialectNamePredicateList:
		destination.write(dialect)
	destination.close()

print("Finished with no errors.")
