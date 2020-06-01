import re
import sys
filename = "maillog"
the_regex = "(([A-Z][a-z][a-z]{1})([\s]*[1]{1}[\s]*)..:([0-5][0-9]):([0-5][0-9])).[a][v][a][s].[p][o][s][t][f][i][x].{14}[a-z]{7}.{6}[a-z]*[[]([0-9.]*)]"
pattern = re.compile("%s" % the_regex, re.I)
open("log2","w").close()
file = open(filename,"r")
mydict = {}
mydict2 = {}
loop_connect = 0
for x in file:
	match = re.search(pattern,x)
	if(match):
		ip_addr = match.group(6)
		if ip_addr not in mydict.keys():
			mydict[ip_addr] = 1
		else:
			score = mydict.get(ip_addr)
			score += 1
			mydict[ip_addr] = score
		loop_connect += 1

sort_orders = sorted(mydict.items(),key=lambda x:x[1],reverse=True)
xyz = 0
largest_ip_addr = ""
largest_ip_num = 0
for x in sort_orders:
	if(xyz == 0):
		largest_ip_addr = x[0]	
		largest_ip_num = x[1]
		xyz = 1
		

f = open("log2","a")
f.write("Total Unknown Connection: %s - [ %s ] accounts for %s\n" % (str(loop_connect), str(largest_ip_addr), str(largest_ip_num)))
print("Total Unknown Connection: " + str(loop_connect) + " - [" + largest_ip_addr + "] accounts for  " + str(largest_ip_num))

file.close()
loop_connect = 0
the_regex2 = "(([A-Z][a-z][a-z]{1})([\s]*[1]{1}[\s]*)[0]{2}:[\d]{2}\D[\d]{2}\s[\w]*\s[a-z/[0-9]*]\W\s[c][a-z]*\s[a-s]*\s[^u][^n]?[A-Z0-9a-z-.]*[[])([0-9.]*)]"
pattern = re.compile("%s" % the_regex2, re.I)
file = open(filename,"r")
for y in file:
	match = re.search(pattern,y)
	if(match):
		ip_addr = match.group(4)
		if ip_addr not in mydict2.keys():
			mydict2[ip_addr] = 1
		else:
			score = mydict2.get(ip_addr)
			score += 1	
			mydict2[ip_addr] = score
		loop_connect += 1

sort_orders = sorted(mydict2.items(),key=lambda x:x[1],reverse=True)
xyz = 0
for x in sort_orders:
	if(xyz == 0):
		largest_ip_addr = x[0]
		largest_ip_num = x[1]
		xyz = 1
f.write("Total Known Connection: %s - [ %s ] accounts for %s\n" % (str(loop_connect),largest_ip_addr,str(largest_ip_num)))
print("Total Known Connection: " + str(loop_connect) + " - [" + largest_ip_addr + "] accounts for " + str(largest_ip_num))
	
file.close()
f.close()
