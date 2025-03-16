from Crypto.Util.number import inverse, long_to_bytes

# Fungsi untuk membaca nilai dari file
def read_values(filename):
    values = {}
    with open(filename, "r") as f:
        for line in f:
            key, value = line.strip().split(": ")
            values[key] = int(value)
    return values

# Fungsi untuk faktorisasi n (mencari p dan q)
def factorize_n(n):
    from sympy import isprime, primerange
    for p in primerange(2, int(n**0.5) + 1):
        if n % p == 0:
            q = n // p
            if isprime(q):  # Pastikan q adalah bilangan prima
                return p, q
    return None, None

# Fungsi dekripsi RSA
def rsa_decrypt(ciphertext, d, n):
    plaintext_int = pow(ciphertext, d, n)
    plaintext = long_to_bytes(plaintext_int)
    return plaintext.decode(errors="ignore")

# Membaca nilai dari file
filename = "values"  # Ubah jika nama file berbeda
values = read_values(filename)

# Ambil nilai c, n, e dari file
c = values["c"]
n = values["n"]
e = values["e"]

# Faktorisasi n untuk mendapatkan p dan q
p, q = factorize_n(n)
if p is None or q is None:
    print("Gagal faktorisasi n. Mungkin n terlalu besar atau bukan hasil kali dua bilangan prima.")
    exit()

# Hitung φ(n)
phi_n = (p - 1) * (q - 1)

# Hitung d (modular inverse dari e)
d = inverse(e, phi_n)

# Dekripsi pesan
decrypted_message = rsa_decrypt(c, d, n)

# Output hasil dekripsi
print("\nPesan setelah dekripsi:", decrypted_message)
