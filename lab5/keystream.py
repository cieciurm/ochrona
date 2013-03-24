import sys

def txt_to_vect(t):
	v = []
	for i in t:
		v.append(ord(i))
	return v

def vect_to_txt(t):
	w = ''
	for i in range(len(t)):
		w += chr(t[i])
	return w.encode("hex")

# permutations
S = []
key = txt_to_vect(sys.argv[1])
# keystream
K = []

for i in range(256):
	S.append(i) # [0, 1, 2, ..., 255]

j = 0
for i in range(256):
	#print j
	#print S[i]
	#print key[i%3]
	j = (j + S[i] + key[i % len(key)]) % 256
	S[i], S[j] = S[j], S[i]

#print S

i = 0
j = 0

for a in range(256):
	i = (i + 1) % 256
	j = (j + S[i]) % 256
	S[i], S[j] = S[j], S[i]
	K.append(S[(S[i] + S[j]) % 256])

#print K
print vect_to_txt(K)
