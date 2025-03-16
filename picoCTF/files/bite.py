def decrypt_flag(how_many_bite):
    encrypted_flag = b'e\x89\x8do\x86`q\x92\x9f]\x92tN\x84zm\x8f[N\x8dyh\x8aqh\x989q\x8d\xb1e\x94\x88\xa3:\xb4l'
    key = how_many_bite.encode()
    decrypted_flag = bytearray()

    for i, c in enumerate(encrypted_flag):
        decrypted_byte = (c - 55) % 256 ^ key[i % len(key)]
        decrypted_flag.append(decrypted_byte)

    return decrypted_flag.decode(errors='ignore')

# Coba dengan input negatif dan non-angka
inputs_to_try = ["-1", "-5", "-10", "abc", "10", "xyz", "not_a_number"]

for input_val in inputs_to_try:
    flag = decrypt_flag(input_val)
    if 'flag{' in flag:
        print(f"Flag ditemukan dengan input '{input_val}': {flag}")
        break
else:
    print("Flag tidak ditemukan dengan input yang dicoba.")

    