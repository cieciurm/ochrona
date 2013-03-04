# liczba szyfrowan potrzebnych do odszyfrowania
# szyfrowaniem o przesunieciu N
#
# NWW(dl. alfabetu, N)/N - 1

x = 26 # dlugosc alfabetu
y = input("Przesuniecie: ")

a = x
b = y

while a != b:
	if a > b:
		a = a-b
	else:
		b = b-a

GCF = a;

LCM = (x*y) / GCF

print "Liczba szyfrowan potrzebna do odszyfrowania: %d" % (LCM/y - 1)
