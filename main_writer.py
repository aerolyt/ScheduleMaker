#Both imports are for web crawling
import urllib
import HTMLParser

#Open in the user-created input file for reading
f = open('input.txt', 'r')

#Initialize the first set of lists
a = []	#This will hold the completed urls
classId = []	#This will hold the file input as separate entries

b = "https://coursebook.utdallas.edu/" #This is the base url
c = "" #The generated url will temporarily be stored in this variable

#For loop to read the input file
for line in f:
	classId.append(line.lower().rstrip('\n'))
	c = str(b) + line.rstrip('\n')
	a.append(str(c))
f.close()

#List to store the web crawl results
urlText = []

#Create parsing class
class parseText(HTMLParser.HTMLParser):
	def handle_data(self, data):
		if data != '\n':
			urlText.append(data)

#Create the s(ASP) script file, and open for writing
newFile = open('main.lp', 'w')

#Create parsing object
lparser = parseText()

#For each element in a, parse the url and save the indexes of benchmark objects in list indices
#In this case, the benchmark string to look for is the term "17S" for 2017 Spring
for i in a:
	lparser.feed(urllib.urlopen(i).read())
	lparser.close()
	indices = []
	indices = [j for j, x in enumerate(urlText) if x == "17S"]

#For each index, retrieve the relevant information and store in temporary result variables
for item in indices:
	result0 = str(urlText[item + 2])
	result2 = str(urlText[item + 6])
	result4 = str(urlText[item + 8])
	result6 = str(urlText[item + 10])
	result7 = str(urlText[item + 11])
	result8 = str(urlText[item + 12])
	
	#Because of varying index positions with different class parameters, we have if statements to ensure the correct information is retrieved.
	if (("HON" in result0 and result8 == " ") or ("HN1" in result0 and result8 == " ")):
		classSection = result0								#classSection stores the course department, number, and section
		classDay = "[" + result4.lower().rstrip(' ') + "]"  #classDay stores the days the class meets on each week, in s(ASP) list format.
		classTime = result6									#classTime stores the time the classes meet, with startTime-endTime
	elif(result7 == " "):
		classSection = result0
		classDay = "[" + result2.lower().rstrip(' ') + "]"
		classTime = result4
	elif("HON" in result0 or "HN1" in result0):
		classSection = result0
		classDay = "[" + result4.lower().rstrip(' ') + "," + result6.lower().rstrip(' ') + "]"
		classTime = result8
	else:
		classSection = result0
		classDay = "[" + result2.lower().rstrip(' ') + "," + result4.lower().rstrip(' ') + "]"
		classTime = result6
	
	#This block of code converts classTime into two separate times, start and end.
	#It also converts the time into military time. 
	classTime = classTime.replace(':', '')
	startTime, endTime = classTime.split('-')
	if 'p' in startTime:
		newStart = startTime[:-2]
		newStart = int(newStart)
		if newStart<1200:
			newStart += 1200
	else:
		newStart = startTime[:-2]
	if 'p' in endTime:
		newEnd = endTime[:-2]
		newEnd = int(newEnd)
		if newEnd<1200:
			newEnd += 1200
	else:
		newEnd = endTime[:-2]
	
	#This statement generates each fact in the s(ASP) output file.
	#The format is _class(course_number, course_number_section, days, time).
	newFile.write('_class(' + classSection[:-9].lower() + classSection[-8:-4] + ", " + classSection[:-9].lower() + classSection[-8:-4] 
		+ classSection[-3:] + ", " + classDay + ", " + str(newStart) + ", " + str(newEnd) + ").\n")

#Generate the include statement and the beginning of the main query
newFile.write("\n#include 'schedule.lp'.\n\n" + "?- _main([")

#Generate the rest of the main query based off of the original user input file
counter = 0
for item in classId:
	newFile.write(item)
	if counter < len(classId)-1:
		newFile.write(", ")
	counter += 1

#Finish the query and close the file. The s(ASP) script is now generated. 
newFile.write("]).")
newFile.close()