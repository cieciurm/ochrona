# for decryption another ARC4 object is necessary

from sys import *
from Crypto.Cipher import ARC4

key = argv[1]
text = argv[2]

cipher = ARC4.new(key)
encrypted = cipher.encrypt(text)

print "RC4(%s, %s) = %s" % (key, text, encrypted.encode("hex"))
