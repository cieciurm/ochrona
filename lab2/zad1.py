import string, fileinput, sys

shift = int(sys.argv[1])

a = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
b = []

for i in range(0, len(a)):
	b.append(a[(shift+i) % 26])

new_alphabet = ''

for i in b:
	new_alphabet += i

table = string.maketrans("abcdefghijklmnopqrstuvwxyz", new_alphabet)

for line in sys.stdin.readlines(): 
        line = line.rstrip()
        print string.translate(line, table)
