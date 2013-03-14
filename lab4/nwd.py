x =  input("1st number: ")
y =  input("2nd number: ")

a = x
b = y

while a != b:
	if a > b:
		a = a - b
	else:
		b = b - a

GCF = a

print "GCF: %d " % GCF
