from pymongo import MongoClient
import random
import os

client = MongoClient(os.environ.get('MONGODB_URI'))
# client = MongoClient("mongodb://localhost:27017")
db = client['database']
post_collection = db["posts"]


with open("flag.txt", 'r') as f:
    flag = f.read()

characters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()'
password = ''.join(random.choice(characters) for i in range(50))

# create the posts
posts = [
    {
        "title": "Lokasi penjualan takjil yang dekat",
        "author": "Salman",
        "note": "Saya tadi nemu pasar yang lagi ramai orang jual takjil",
        "location": "Jl. Kota Bambu Raya No.99 5, RT.5/RW.5",
        "password": False
    },
    {
        "title": "Takjil di sini pada murah murah guys",
        "author": "Adam",
        "note": "Tadi lagi pulang sholat jumat nemu Masjid yang ",
        "location": "Masjid Agung Al-Azhar",
        "password": "TakjilKuPastiAman"
    },
    {
        "title": "Di pasar ini rame juga",
        "author": "Dimas",
        "note": "Habis berburu, nemu pasar yang rame juga",
        "location": "Pasar Benhil",
        "password": False
    },
    {
        "title": "Lokasi beli takjil favoritku",
        "author": "Max",
        "note": flag,
        "location": "Jl. Taman Wijaya Kusuma, Ps. Baru, Kecamatan Sawah Besar",
        "password": password
    },
    {
        "title": "Jalan Soka lagi rame nih",
        "author": "James",
        "note": "Tadi habis pulang kerja, nemu jalan yang lagi rame",
        "location": "Jalan Soka",
        "password": False
    },
    {
        "title": "Masjid yang cukup rame saat jualan takjil",
        "author": "Sinta",
        "note": "Kalau ada yang mau beli lemper, risol, dll, di sini banyak",
        "location": "Masjid Sunda Kelapa",
        "password": "Password1234"
    }
]

post_collection.insert_many(posts)
config = db["config"]
config.insert_one({"installed": True})