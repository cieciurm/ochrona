import sys, re, string, operator
from math import log

stat = {}

allchar = 0.0
entropy = 0.0

for line in sys.stdin.readlines():
	line = re.sub(r'\s', '', line)
	for znak in line:
		if znak in stat:
			stat[znak] += 1
		else:
			stat[znak] = 1
		allchar += 1

for znak in stat:
	stat[znak] = stat[znak]/allchar
	entropy += stat[znak] * log(stat[znak], 2)

entropy *= -1

print "Entropy == %g" % entropy
