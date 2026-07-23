"""
Tugas Pertemuan 4 -  customisasi representasi objek serta 
mendefinisikan logika perbandingan (comparison logic) antar objek secara mandiri.
File: main.py

"""
# pertemuan_4/main.py

class Produk:
    # 1. Special Method: __init__
    def __init__(self, nama, harga, stok):
        self.nama = nama
        self.harga = harga
        self.stok = stok

    # 2. Special Method: __str__ (Representasi teks saat objek di-print)
    def __str__(self):
        return f"Produk: {self.nama} | Harga: Rp{self.harga:,} | Stok: {self.stok} unit"

    # 3. Special Method Perbandingan 1: __eq__ (Sama dengan / ==)
    def __eq__(self, other):
        if isinstance(other, Produk):
            return self.harga == other.harga
        return False

    # 4. Special Method Perbandingan 2: __lt__ (Lih kecil dari / <)
    def __lt__(self, other):
        if isinstance(other, Produk):
            return self.harga < other.harga
        return NotImplemented

    # 5. Special Method Perbandingan 3: __gt__ (Lebih besar dari / >)
    def __gt__(self, other):
        if isinstance(other, Produk):
            return self.harga > other.harga
        return NotImplemented


# ==========================================
# INSTANSIASI DAN PENGUJIAN
# ==========================================

if __name__ == "__main__":
    print("=== 1. INSTANSIASI DAN PENGUJIAN __str__ ===")
    # Memilih minimal 3 Object dengan data berbeda
    produk_a = Produk("Laptop Gaming", 15000000, 5)
    produk_b = Produk("Smartphone Flagship", 15000000, 10)
    produk_c = Produk("Wireless Earbuds", 1500000, 25)

    # Menguji method __str__ dengan melakukan print pada objek
    print(produk_a)
    print(produk_b)
    print(produk_c)
    print()

    print("=== 2. PENGUJIAN METODE PERBANDINGAN ===")
    # Menguji __gt__ (>)
    print(f"Apakah {produk_a.nama} > {produk_c.nama}? -> {produk_a > produk_c}")

    # Menguji __lt__ (<)
    print(f"Apakah {produk_c.nama} < {produk_b.nama}? -> {produk_c < produk_b}")

    # Menguji __eq__ (==)
    print(f"Apakah harga {produk_a.nama} == {produk_b.nama}? -> {produk_a == produk_b}")
    print(f"Apakah harga {produk_a.nama} == {produk_c.nama}? -> {produk_a == produk_c}")