import re
import sys
regex = "(([A-Z][a-z][a-z]{1})([\s]*[1]{1}[\s]*)[0]{2}:[\d]{2}\D[\d]{2}\s[a-z]{4}\s[a-z]{7}/[a-z]{5}[[][0-9]*[]:\s0-9A-Z]*[r][a-z:\s]*\s[A-Z]*\s[a-z.0-9-\s]*[[])([0-9.]*)[]:\s0-9A-Za-z;[]*[0-9.]*[]\s]*[a-z]*\s[a-z]{5}\s[a-z]{5}.[a-z]{5}.[a-z;\s]{5}[-A-Za-z\s://.?=0-9;]*[<]([a-zA-Z_0-9@.]*)>\s[a-z]{2}=<([a-zA-Z@.]*)>"
filename = "maillog"
open("log4","w").close()
pattern = re.compile("%s" % regex, re.I)
file = open(filename,"r")
from_addr_list = []
to_addr_list = []
ip_addr_list = []
match_rejected = 0
for x in file:
	match = re.search(pattern,x)
	if(match):
		ip_addr = match.group(4)
		if ip_addr not in ip_addr_list:
			ip_addr_list.append(ip_addr)
		from_addr = match.group(5)
		if from_addr not in from_addr_list:
			from_addr_list.append(from_addr)
		to_addr = match.group(6)
		if to_addr not in to_addr_list:
			to_addr_list.append(to_addr)
		match_rejected += 1

f = open("log4","a")
f.write("%d messages rejected\n" % match_rejected)
print("%d messages rejected\n" % match_rejected)
f.write("%d unique IP's\n" % len(ip_addr_list))
print("%d unique IP's\n" % len(ip_addr_list))
f.write("%d unique from addresses\n" % len(from_addr_list))
print("%d unique from addresses\n" % len(from_addr_list))
f.write("%d unique to addresses\n" % len(to_addr_list))
print("%d unique to addresses\n" % len(to_addr_list))
f.close()
