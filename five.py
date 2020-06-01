from shutil import copyfile
import re
import sys
filename = sys.argv[1]
length_arguments = len(sys.argv)
list_arg = []
for xyz in sys.argv[2:]:
	list_arg.append(xyz)

file = open(filename, "r")
filename2 = "fake_log"
file2 = open(filename2, "w")
for x in file:
	for y in list_arg:
		if y not in x:
			file2.write("%s\n" % x)
	
file2.close()
file.close()
copyfile(filename2,filename)

			
	
