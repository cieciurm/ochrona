from Crypto.PublicKey import RSA
import sys

# Tworzenie kluczy RSA
rsa_keys = RSA.generate(1024)

# Wydzielenie klucza publicznego
pub_key = rsa_keys.publickey()
print "n=",rsa_keys.publickey().n
print "e=",rsa_keys.publickey().e
print "d=",rsa_keys.d
print "n=",rsa_keys.n

# Zaszyfrowanie przy pomocy klucza publicznego
encrypted = pub_key.encrypt(sys.argv[1], "abc")

# Odszyfrowanie kluczem prywatnym
print rsa_keys.decrypt(encrypted)
