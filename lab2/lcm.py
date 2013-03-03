#
# liczba szyfrowan potrzebnych do odszyfrowania
# szyfrowaniem o przesunieciu N
#
# NWW(dl. alfabetu, N)/N - 1
#


x =  input("1st number: ")
y =  input("2nd number: ")

a = x
b = y

while a != b:
	if a > b:
		a = a-b
	else:
		b = b-a

GCF = a;

LCM = (x*y) / GCF

print "LCM: ", LCM
