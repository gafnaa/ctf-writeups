# Lagi dan Lagi

## Deskripsi Soal

Lagi Dan lagi gambar mimin tiba tiba berubah menjadi tulisan acak, mimin tidak tau harus apa bantu mimin Dong

https://ctf.rajawalisecteam.eu.org/assets/uploads/hidelagi.txt

## Solusi

Setelah link dibuka, ditemukan banyak tulisan acak, sepertinya itu merupakan file gambar yang isinya telah dienkripsi menggunakan base64. 

Lalu, saya membuat sebuah program untuk mengkonversi kode tersebut lalu menyimpannya sebagai file gambar.

```python
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
```

## Flag

    CTFRST{h1de_1m4g3_w1th_b4se}


