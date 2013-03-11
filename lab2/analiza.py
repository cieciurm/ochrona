import sys, re, string, operator

stat = {}
for line in sys.stdin.readlines():
        line = re.sub(r'\s', '', line)
        for znak in line:
                if znak in stat:
                        stat[znak] += 1
                else:
												# tu bylo 0 (???)
                        stat[znak] = 1


for znak in stat:
        print "%s <=> %d " % (znak, stat[znak])
