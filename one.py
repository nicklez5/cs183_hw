import sys
import re

filename = str(sys.argv[1])
textfile = open(filename, "r")
filetext = textfile.read()
textfile.close()
matches = re.findall("rejected",filetext)

a = 0
for match in matches:
	a += 1

	

