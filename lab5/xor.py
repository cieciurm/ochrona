from operator import xor
from sys import *

a = int(argv[1])
b = int(argv[2])

bin_a = bin(a)
bin_b = bin(b)

max_len = 0;

if len(bin_a) >= len(bin_b):
	max_len = len(bin_a)
else:
	max_len = len(bin_b)

print bin(a).zfill(max_len),"   ==",a
print bin(b).zfill(max_len),"   ==",b

print "(XOR)-----------------------"

result = a^b
print bin(result).zfill(max_len),"   ==",result
