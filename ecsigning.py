from ecdsa import SigningKey, NIST256p
from hashlib import sha256

# Generate a private key (Signing Key) and its corresponding public key (Verifying Key)
sk = SigningKey.generate(curve=NIST256p, hashfunc=sha256)
vk = sk.get_verifying_key()

# Convert the keys to hexadecimal strings
private_key_hex1 = sk.to_string().hex()
public_key_hex1 = vk.to_string().hex()

# Output the keys as hexadecimal strings
print("Private Key (Hex):", private_key_hex1)
print("Public Key (Hex):", public_key_hex1)



# sign_message.py

from ecdsa import SigningKey, VerifyingKey, NIST256p
from hashlib import sha256

# Hexadecimal strings of the private key and public key (replace with actual values from generate_keys.py)
private_key_hex = private_key_hex1
public_key_hex = public_key_hex1

# Convert the hexadecimal strings back to bytes
private_key_bytes = bytes.fromhex(private_key_hex)
public_key_bytes = bytes.fromhex(public_key_hex)

# Reconstruct the SigningKey (private key) and VerifyingKey (public key) from bytes
sk = SigningKey.from_string(private_key_bytes, curve=NIST256p, hashfunc=sha256)
vk = VerifyingKey.from_string(public_key_bytes, curve=NIST256p, hashfunc=sha256)

# Message to be signed
message = b"Message"

# Sign the message
signature = sk.sign(message)

# Convert the signature to hexadecimal
signature_hex = signature.hex()

# Output the signature as a hexadecimal string
print("Signature (Hex):", signature_hex)
