# verify_signature.py

from ecdsa import VerifyingKey, NIST256p
from hashlib import sha256
from ecdsa import BadSignatureError

# Hexadecimal strings of the private key, public key, and signature (you can replace these with the actual values)
private_key_hex = "eb35431dcaa849be704965f384a2e4df1d6d933099d8f5d23042b9777cdf95f1"
public_key_hex = "a9e7a85bdfe36b98fbfd2d053a1002d5d5c20486cc08372129028cc73c3edd62627fa60ac80050c8f867c681a0d18f2754511db754547067a15a3ad2c58c0391"
signature_hex = "5b7f9f113221418f00566080f41d05c66d0f8e734157c3f264cf4b4ef2f1c09b1353a119cfdf32e48c4f1611cc4d1efe5922b42ec3c230dd2db13e4e11297272"

# Message to verify
message = b"Messagea"

# Convert hexadecimal strings back to bytes
private_key = bytes.fromhex(private_key_hex)
public_key = bytes.fromhex(public_key_hex)
signature = bytes.fromhex(signature_hex)

# Reconstruct the verifying key from the public key
vk = VerifyingKey.from_string(public_key, curve=NIST256p, hashfunc=sha256)

# Verify the signature
try:
    vk.verify(signature, message)
    print("Signature is valid.")
except BadSignatureError:
    print("Invalid signature.")
