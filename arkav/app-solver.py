# Given encrypted flag
enc_flag = b't;*1:\x12T\x14\x1f<$\x0c&--.}68\x113\x11-\x07-\x18D,W5U"j \x0f7)==D<+VU>"\x13^E\x0c\x13$\x15\'\x1bA-\r\x0f\x03\x1c'

# Known parts of the flag
known_flag = "ARKAV{"
known_flag += "}"  # The last character is '}'

# XOR the known parts of the flag with the encrypted flag to get parts of the key
key_parts = []
for i in range(len(known_flag)):
    key_parts.append(chr(enc_flag[i] ^ ord(known_flag[i])))

# The key is 16 characters long, so we need to find the remaining characters
# Let's assume the key is "ARKAV{REDACTED}" and try to recover it
# We can try to brute force the remaining characters

# Let's try to recover the full key
key = ""
for i in range(16):
    if i < len(key_parts):
        key += key_parts[i]
    else:
        # Try to guess the remaining characters
        # For simplicity, let's assume the key is "ARKAV{REDACTED}"
        key += "A"  # Placeholder, you can try other characters

# Now, let's try to decrypt the flag using the recovered key
def xor_decrypt(encrypted: bytes, key: str) -> str:
    key = key * (len(encrypted) // len(key)) + key[: len(encrypted) % len(key)]
    return "".join(chr(a ^ ord(b)) for a, b in zip(encrypted, key))

decrypted_flag = xor_decrypt(enc_flag, key)
print(f"Decrypted Flag: {decrypted_flag}")

# If the decrypted flag doesn't make sense, try adjusting the key