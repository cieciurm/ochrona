import sys

def txt_to_vect(t):
	"""Transforms a string into a ASCII codes vector"""
	v = []
	for i in t:
		v.append(ord(i))
	return v

def vect_to_txt(t):
	"""Transforms a ASCII codes vector into a string"""
	w = ''
	for i in range(len(t)):
		w += chr(t[i])
	return w.encode("hex")

def rc4_keystream_generate(k):
	"""Generates a RC4 cipher keystream based on a key"""
	S = [] # permutations
	key = txt_to_vect(k)
	K = [] # keystream

	for i in range(256):
		S.append(i) # [0, 1, 2, ..., 255]

	j = 0
	for i in range(256):
		j = (j + S[i] + key[i % len(key)]) % 256
		S[i], S[j] = S[j], S[i]

	i = j =  0

	for a in range(256):
		i = (i + 1) % 256
		j = (j + S[i]) % 256
		S[i], S[j] = S[j], S[i]
		K.append(S[(S[i] + S[j]) % 256])
	return vect_to_txt(K)

if __name__ == "__main__":
	key = sys.argv[1]
	print rc4_keystream_generate(key)
