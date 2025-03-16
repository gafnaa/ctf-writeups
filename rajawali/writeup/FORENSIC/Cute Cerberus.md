# Cute Cerberus

## Deskripsi Soal

Cari tau dimana aku bersembunyi!

https://ctf.rajawalisecteam.eu.org/assets/uploads/cute_cerberus.jpg

## Solusi

Karena file berupa gambar, kita cek metadata nya apakah ditemukan petunjuk,di sini saya menggunakan ```exiftool``` untuk mengeceknya. Setelah dicek, ternyata ditemukan sesuatu pada bagian **Copyright** karena isinya sepertinya dienkripsi menggunakan base4.

Kemudian, dilakukan decode dan ditemukan flag

[![cute.png](https://i.postimg.cc/HxxhrtWb/cute.png)](https://postimg.cc/Y453VYWS)

## Flag
    CTFRST{s0N_0f_h4D35}
    
