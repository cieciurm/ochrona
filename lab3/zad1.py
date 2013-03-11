import sys, string, crypt, random

random.seed()

htpasswd = open("htpasswd")
user = sys.argv[1]

users = {}

for line in htpasswd.readlines():
	tmp = line.split(":")
	users[tmp[0]] = tmp[1]
	if user in line:
		split = line.split(":")
		old_pass = split[1]
		salt = old_pass[:2]

		#print "Sol:", salt
		#print "Stare haslo:", old_pass

		trail = raw_input("Podaj stare haslo: ")
		trail_pass = crypt.crypt(trail, salt)
		trail_pass += "\n"
		if trail_pass == old_pass:
			print "Poprawne haslo."
		else:
			print "Niepoprawne haslo."
			sys.exit()

		new_pass = raw_input("Podaj nowe haslo: ")

		new_salt = chr(random.randint(65, 121)) + chr(random.randint(65, 121))
		#new_salt = new_pass[:2]

		new_crypted_pass = crypt.crypt(new_pass, new_salt)
		new_crypted_pass += "\n"
		#print new_crypted_pass

users[user] = new_crypted_pass

new_htpasswd = open("htpasswd_new", "w");

for element in users:
	new_htpasswd.write(element)
	new_htpasswd.write(":")
	new_htpasswd.write(users[element])
