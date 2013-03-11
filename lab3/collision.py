import sys

def trivial_hash(dane):
	hash = 0
	for znak in dane:
		hash += ord(znak)
	return hash % 999

w1 = sys.argv[1]
w2 = sys.argv[2]
h1 = trivial_hash(w1)
h2 = trivial_hash(w2)

print "%s => %d" % (w1, h1)
print "%s => %d" % (w2, h2)

if h1 == h2:
	print "Kolizja"
else:
	print "Nie kolizja"
