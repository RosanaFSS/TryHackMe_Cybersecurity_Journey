import hashlib
from sympy import nextprime
from Crypto.PublicKey import RSA
from Crypto.Signature import pss
from Crypto.Hash import SHA256

# Add the user name
loveuser = "username"

# Add the message sent by the user
lovemessage = "message"

def keygeneration():
    print(f"\n _______________________________________________________________________________________")
    print(f"\n                            Calculating {loveuser} key")
    print(f"\n _______________________________________________________________________________________")
    lovestring = f"{loveuser}_lovenote_2026_valentine"
    lovebytes = lovestring.encode('utf-8')
    
    prepp = hashlib.sha256(lovebytes).hexdigest()
    p = nextprime(int(prepp, 16))
    print(f"\n                            p         : {p}")
  
    prepq = hashlib.sha256(lovebytes + b"pki").hexdigest()
    q = nextprime(int(prepq, 16))
    print(f"\n                            q         : {q}")
    
    n = p * q
    print(f"\n                            n         : {n}")
  
    e = 65537
    print(f"\n                            e         : {e}")
  
    phi = (p - 1) * (q - 1)
    print(f"\n                            phi       : {phi}")
  
    d = pow(e, -1, phi)
    print(f"\n                            d         : {d}")
    print(f"\n _______________________________________________________________________________________")
    
    return RSA.construct((n, e, d))

def signaturecalculation(key, lovemessage):
    h = SHA256.new(lovemessage.encode('utf-8'))
    lovebits = key.size_in_bits()
    lovelength = (lovebits - 1 + 7) // 8 
    lovesalt = lovelength - h.digest_size - 2
    print(f"\n\n\n _______________________________________________________________________________________")
    print(f"\n                            Size      : {lovebits} bits")
    print(f"\n                            Length    : {lovelength} bytes")
    print(f"\n                            Salt      : {lovesalt} bytes")
    print(f"\n _______________________________________________________________________________________")
    
    if lovesalt < 0:
        raise ValueError("Key is too small even for 0 salt!")

    signer = pss.new(key, salt_bytes=lovesalt)
    signature = signer.sign(h)
    
    return signature.hex()

try:
    admin_key = keygeneration()
    signature = signaturecalculation(admin_key, lovemessage)
    
    print(f"\n\n _______________________________________________________________________________________")
    print(f"\n                              Signature : {signature} ")
    print(f"\n\n _______________________________________________________________________________________")

except Exception as e:
    print(f"\n                             Error     : {e}")
