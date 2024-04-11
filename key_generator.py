from ecdsa import SigningKey, SECP256k1

# Generate a key pair
sk = SigningKey.generate(curve=SECP256k1)
vk = sk.get_verifying_key()

# Get the private and public keys in hex format
private_key_hex = sk.to_string().hex()
public_key_hex = vk.to_string().hex()

print('Private key:', private_key_hex)
print('Public key:', public_key_hex)
