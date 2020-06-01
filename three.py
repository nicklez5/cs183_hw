import re
import sys
_regex = "(([A-Z][a-z][a-z]{1})([\s]*[1]{1}[\s]*)[0]{2}:[\d]{2}\D[\d]{2}\s[a-z]{4}\s[a-z]{6}[[][0-9]{4}][-,:(0-9)\sA-Za-z]*[<])([0-9-a-zA-Z=.@_]*)[-><\s]*([a-zA-Z0-9@.]*)>"
pattern = re.compile("%s" % _regex, re.I)
filename = sys.argv[1]
to_dict={}
from_dict={}
file = open(filename,"r")
for x in file: 
	match = re.search(pattern,x)
	if(match):
		from_addr = match.group(4)
		if from_addr not in from_dict.keys():
			from_dict[from_addr] = 1
		else:
			score = from_dict.get(from_addr)
			score += 1
			from_dict[from_addr] = score

		to_addr = match.group(5)

		if to_addr not in to_dict.keys():
			to_dict[to_addr] = 1
		else:
			score2 = to_dict.get(to_addr)
			score2 += 1
			to_dict[to_addr] = score2

sort_orders = sorted(from_dict.items(),key=lambda x:x[1],reverse=True)
xyz = 0
from_email = ""
from_counter = 0
index_counter = 0
for x in sort_orders:
	if(xyz == 0):
		from_email = x[0]
		from_counter = x[1]
		xyz = 1
	if(index_counter < 5):
		print("From %s %d\n" % (x[0],x[1]))
	index_counter += 1

	
sort_order2 = sorted(to_dict.items(), key=lambda x:x[1],reverse=True)
xyz = 0
to_email = ""
to_counter = 0
index_counter = 0
for x in sort_order2:
	if(xyz == 0):
		to_email = x[0]
		to_counter = x[1]
		xyz = 1
	if(index_counter <  5):
		print("To %s %d\n" % (x[0],x[1]))
	index_counter += 1

file.close()


