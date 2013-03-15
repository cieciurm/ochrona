import sys, math

# szukaj liczb pierwszych w przedziale [2; sys.argv[1]]

primes = []
n = int(sys.argv[1])

print "* Szukam liczb pierwszych w przedziale [2; %d]" % (n)

# wyplenij tablice liczbami [2; n]

for i in range(2, n+1):
	primes.append(i)


# usun wielokrotnosci kolejnych liczb az do sqrt(n)

j = primes[0] # od 2
while j <= math.sqrt(n):
	for i in primes:
		if i % j == 0 and i != j:
			#print "%d dzieli %d, usuwam %d" % (j, i, i)
			primes.remove(i)
	j += 1

# wypisz liste liczb pierwszych

print primes
