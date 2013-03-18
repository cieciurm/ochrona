import sys

word = sys.argv[1]
size = int(sys.argv[2])

# zamiana wejscia na jeden string
# kod ascii dopelniane do 3 charow

vector = ''

for i in range(0, len(word)):
	if ord(word[i])/100 == 1 or ord(word[i])/100 == 2:
		vector += str(ord(word[i]))
	else:
		vector += '0' + str(ord(word[i]))

# dodawanie do nowego wektora
# bloki o dlugosci podanej

vector2 = []
elem = ''
max_index = 0

for i in vector:
	elem += i
	if len(elem) == size:
		#print elem
		vector2.append(elem)
		max_index += 1
		elem = ''

elem = ''

# doklejanie ostatniego elementu
# ew. dopelnianie zerami na koncu

if len(vector) % size != 0:
	for i in range(max_index*size, len(vector)):
		elem += vector[i]
	while len(elem) != size:
		elem += '0'
	vector2.append(elem)

print "dlugosc bloku = %d" % size
print word, "==", vector2
