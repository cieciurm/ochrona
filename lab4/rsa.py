from Crypto.PublicKey import RSA

# Tworzenie kluczy RSA
rsa_keys = RSA.generate(1024)

# Wydzielenie klucza publicznego
pub_key = rsa_keys.publickey()

# Zaszyfrowanie przy pomocy klucza publicznego
encrypted = pub_key.encrypt("Top secret", "some randomness")

# Odszyfrowanie kluczem prywatnym
print rsa_keys.decrypt(encrypted)
