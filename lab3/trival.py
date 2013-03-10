import sys

def trivial_hash(dane):
	hash = 0
	for znak in dane:
		hash += ord(znak)
	return hash % 999

print trivial_hash(sys.argv[1])
