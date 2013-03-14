import sys

word = ''
vector = []

for i in range(1, len(sys.argv)):
	vector.append(int(sys.argv[i]))

for j in range (0, len(vector)):
	word += chr(vector[j])

print vector ,"==", word
