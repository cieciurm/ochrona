import sys, re, string, operator

stat = {}

allchar = 0.0
for line in sys.stdin.readlines():
	line = re.sub(r'\s', '', line)
	for znak in line:
		if znak in stat:
			stat[znak] += 1
		else:
			stat[znak] = 1
		allchar += 1

#print allchar

for znak in stat:
        print "%s <=> %d/%d == %f%% " % (znak, stat[znak], allchar, stat[znak]/allchar*100)
