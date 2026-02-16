# Script learned in TryHachMe Breaking RSA room
# Retrieve modulus (n) and public exponent (e)

#!/usr/bin/env python3
from Crypto.PublicKey import RSA

# Save the Public Key in a file named "id_rsa.pub"
f = open("id_rsa.pub", "r")

key = RSA.importKey(f.read())

n = key.n
e = key.e

print(f"   Modulus (n)           : {n}")
print(f"   Public Exponent (e)   : {e}")
