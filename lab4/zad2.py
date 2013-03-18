from prime import *
import random
from euklides import *

def wzglednie_pierwsze(a,b):
	if euklides(a,b) == 1:
		return True
	else:
		return False

def odwr_mod(a, n):
	p0, p1, a0, n0 = 0, 1, a, n
	q, r = n0 // a0, n0 % a0
	while r:
		t = p0 - q * p1
		if t >= 0:
			t = t % n
		else:
			t = n - ((-t) % n)
			p0, p1, n0, a0 = p1, t, a0, r
			q, r  = n0 // a0, n0 % a0
			return p1

############################

p = random.randint(1, 100)
q = random.randint(1, 100)

while is_prime(p) and is_prime(q):
	p = random.randint(1, 100)
	q = random.randint(1, 100)

n = p*q

euler = (p-1)*(q-1)

e = random.randint(1, euler)
while wzglednie_pierwsze(e, euler) != True:
	e = random.randint(1, euler)

d = odwr_mod(e,euler)

print "p=",p
print "q=",q
print "n=p*q=",n
print "euler=(p-1)*(q-1)=",euler
print "e=wzglednie pierwsza z euler z przedzialu [1; euler]=",e
print "d=e^(-1) modulo euler=",d
print ""
print "Klucz publiczny : n=%d,e=%d" % (n,e)
print "Klucz prywatny  : n=%d,d=%d" % (n,d)
