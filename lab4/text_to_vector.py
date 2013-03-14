import sys

word = sys.argv[1]
vector = []

for i in range(0, len(word)):
	vector.append(ord(word[i]))

print word, "==", vector
