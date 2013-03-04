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

max = 0
max_znak = ''

for znak in stat:
	if stat[znak] > max:
		max = stat[znak]
		max_znak = znak

a = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

#print "Najczesciej wystepujacy znak: %s (%d)" % (max_znak, max)
print "Przesuniecie wynosi: %s" % (a.index(max_znak) - a.index('e'))
