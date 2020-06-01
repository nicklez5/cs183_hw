import sys
import re
start_index = 0
the_regex = ".*(([A-Z][a-z][a-z]{1})([\s]*[1]{1}[\s]*)..:([%d][%d]):([0-5][0-9])).*" % (start_index/10,start_index % 10)
open("hourlyinfo.txt","w").close()
pattern = re.compile("%s" % the_regex, re.I)
filename = sys.argv[1]
num_reject = 0
num_quarantine = 0
file = open(filename,"r")
for x in file:
	match = re.search(pattern,x)
	if(match): 
		temporary_string = match.group(0)
		if "reject" in temporary_string:
			num_reject += 1
		if "quarantine" in temporary_string:
			num_quarantine += 1
	else:
		f = open("hourlyinfo.txt","a")
		f.write("Mar 1 00:%d%d   [postfix rejects:%d]   [amavis quarantines:%d]\n" % (start_index/10,start_index % 10, num_reject, num_quarantine))
		f.close()
		num_quarantine = 0
		num_reject = 0
		start_index += 1
		the_regex = ".*(([A-Z][a-z][a-z]{1})([\s]*[1]{1}[\s]*)..:([%d][%d]):([0-5][0-9])).*"% (start_index/10, start_index % 10)
		pattern = re.compile("%s" % the_regex, re.I)
				
	

		


print("Number of Rejects: " + str(num_reject))
print("Number of Quarantine: " + str(num_quarantine))

	

