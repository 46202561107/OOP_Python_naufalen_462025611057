"""
Tugas Pertemuan 2 -  pendefinisian Class, pembuatan Object, dan juga
mengelola lingkungan kerja Python menggunakan Virtual Environment (venv).
File: main.py
"""
# main.py

# 1. Pendefinisian Class
class Laptop:
    # Minimal 3 Attributes (merk, prosesor, ram)
    def __init__(self, merk, prosesor, ram):
        self.merk = merk
        self.prosesor = prosesor
        self.ram = ram

    # Method pendukung untuk merestruktur output menjadi 1 baris teks
    def get_info(self):
        return f"Laptop {self.merk} | Prosesor: {self.prosesor} | RAM: {self.ram} GB"


# 2. Pembuatan minimal 2 Object dari Class yang sama
laptop1 = Laptop("Asus ROG", "Intel i7", 16)
laptop2 = Laptop("MacBook Air", "Apple M2", 8)

# 3. Menampilkan ke console (1 print untuk 1 object)
print(laptop1.get_info())
print(laptop2.get_info())
