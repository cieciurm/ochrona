#
# liczy srednia liczbe porownan przy lamaniu
# hasla 3 znakowego metoda bruteforce 
# --- przyjmuje liczbe powtorzen jako argv[1]
#

import string, sys, random

random.seed()

letters = string.ascii_letters
all_spins = 0
n = int(sys.argv[1])


for i in range(1, n):
	spins = 0
	x = letters[random.randint(1, 51)]
	y = letters[random.randint(1, 51)]
	z = letters[random.randint(1, 51)]
	password = x+y+z

	for a in letters:
		for b in letters:
			for c in letters:
				trail = a+b+c
				spins += 1
				if trail == password:
					all_spins += spins
					break

print all_spins/n
