import sys
import re

filename = sys.argv[1]
num_reject = 0
num_quarantine = 0
with open(filename) as fp:
	line = fp.readline()
	match = re.search(.*(([A-Z][a-z][a-z]{1})([\s]*[1]{1}[\s]*)..:([0][0]):([0-5][0-9])).*/g,line)
	if match:
		selected_string = match.string()
		if "reject" in selected_string:
			num_reject += 1
		elif "quarantine" in selected_string:
			num_quarantine += 1
		
fp.closed
print("Number of Rejects: " + num_reject)
print("Number of Quarantine: " + num_quarantine)

	

