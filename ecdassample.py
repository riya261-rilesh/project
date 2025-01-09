import  ecdsa
from hashlib import sha256
sk=ecdsa.SigningKey.generate(curve=ecdsa.SECP256k1,hashfunc=sha256)
vk=sk.get_verifying_key()
print(sk.privkey)
print(vk)
sig= sk.sign(b"Message")
s=vk.verify(sig,b"Message")
print(s)

