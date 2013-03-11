import sys, hashlib

file = open(sys.argv[1])

sum = ''

for line in file.readlines():
	sum += line

#print sum 
checksum = hashlib.md5(sum)

print checksum.hexdigest()
