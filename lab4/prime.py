import sys

def is_prime(a):
	divisors = 0
	for i in range(1, a+1):
		if a % i == 0:
			print "+ %d jest dzielnikiem" % i
			divisors += 1
			if divisors > 2:
				print "! Liczba ma juz co najmniej 3 dzielniki!"
				return False
	return True

if __name__ == "__main__":
	a = int(sys.argv[1])
	if is_prime(a):
		print "Jest pierwsza."
	else:
		print "Nie jest pierwsza."
