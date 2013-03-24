import sys, re, string
from math import log

def calculate_entropy():
	stat = {}     # dictionary - chars and number of repetitions
	allchar = 0.0 # total number of characters
	entropy = 0.0 # initial entropy

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
	return entropy

if __name__ == "__main__":
	print "Entropy == %g" % calculate_entropy()
