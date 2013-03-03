import string, fileinput

shift = input("Podaj przesuniecie: ")

a = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
b = []

for i in range(0, len(a)):
	b.append(a[(shift+i) % 26])

#print a
#print b

new_alphabet = ''

for i in b:
	new_alphabet += i

#print new_alphabet

#print "Wpisz tekst do zaszyfrowania:"

table = string.maketrans("abcdefghijklmnopqrstuvwxyz", new_alphabet)

for line in fileinput.input():
        line = line.rstrip()
        print string.translate(line, table)
