import string, sys

password = sys.argv[1]
letters = string.ascii_letters
spins = 0

print "~* Brutalny lamacz hasel trojznakowych (male i duzelitery) *~"
print "~* Twoje haslo to: %s *~" % (password)

for a in letters:
	for b in letters:
		for c in letters:
			trail = a+b+c
			spins += 1
			if trail == password:
				print "Zlamano haslo (%s) - %d porownan!" % (a+b+c, spins)
				sys.exit()

print "Nie zlamano hasla :(!"
