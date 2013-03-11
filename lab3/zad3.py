import string, sys, crypt

htpasswd = sys.argv[1]
user = sys.argv[2]
letters = string.ascii_letters

file = open(htpasswd)

for line in file.readlines():
	if user in line:
		splits = line.split(":")
		password = splits[1]
		salt = password[:2]
		#print password
		#print salt

		for a in letters:
			for b in letters:
				for c in letters:
					trail = a+b+c

					if (crypt.crypt(trail, salt)+"\n") == password:
						print "Zlamano haslo (%s)" % (a+b+c)
						sys.exit()
