import hashlib

username = b"PRITCHARD"
hashed = hashlib.sha256(username).hexdigest()

dynamic_part = hashed[4] + hashed[5] + hashed[3] + hashed[6] + hashed[2] + hashed[7] + hashed[1] + hashed[8]
license_key = f"picoCTF{{1n_7h3_|<3y_of_{dynamic_part}}}"

print("License Key:", license_key)
