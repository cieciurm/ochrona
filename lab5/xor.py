import sys

def xor_numbers(a, b):
	"""XORs two decimal numbers and produces a result as a decimal aswell"""
	bin_a = bin(a)
	bin_b = bin(b)
	#max_len = 0;
	#if len(bin_a) >= len(bin_b):
		#max_len = len(bin_a)
	#else:
		#max_len = len(bin_b)
	#print bin(a).zfill(max_len),"   ==",a
	#print bin(b).zfill(max_len),"   ==",b
	#print "(XOR)-----------------------"
	result = a^b
	#print bin(result).zfill(max_len),"   ==",result
	return result

def xor_string(a, b):
	"""XORs two string produces a result as a string aswell"""
	v = [chr(ord(a) ^ ord(b)) for a, b in zip(a, b)]
	return ''.join(v).encode("hex")

if __name__ == "__main__":
	print xor_numbers(65, 98)
	print xor_string(sys.argv[1], sys.argv[2])
