import base64

# Path file yang diunggah
input_file_path = "lagilagi.txt"
output_image_path = "lagilagi.png"

# Membaca file Base64 dan menyimpannya sebagai gambar
with open(input_file_path, "r") as file:
    base64_data = file.read()

# Menghapus potensi header Base64 (jika ada)
if "," in base64_data:
    base64_data = base64_data.split(",")[1]

# Decode Base64 menjadi binary
image_data = base64.b64decode(base64_data)

# Simpan sebagai file gambar
with open(output_image_path, "wb") as img_file:
    img_file.write(image_data)

# Mengembalikan path gambar yang telah disimpan
output_image_path
