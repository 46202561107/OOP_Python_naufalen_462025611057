# Pertemuan_3/main.py

class Karyawan:
    def __init__(self, nama, posisi, gaji_pokok):
        # Attributes
        self.nama = nama
        self.posisi = posisi
        self.gaji_pokok = gaji_pokok

    # --- INSTANCE METHODS (Menggunakan 'self') ---
    
    # Instance Method 1: Menampilkan profil/informasi karyawan
    def tampilkan_profil(self):
        return f"Karyawan: {self.nama} | Posisi: {self.posisi} | Gaji Pokok: Rp{self.gaji_pokok:,}"

    # Instance Method 2: Menghitung total gaji setelah ditambahkan bonus persentase
    def hitung_total_gaji(self, persentase_bonus):
        bonus = self.gaji_pokok * (persentase_bonus / 100)
        total = self.gaji_pokok + bonus
        return f"Total Gaji {self.nama} (+Bonus {persentase_bonus}%): Rp{int(total):,}"

    # --- STATIC METHOD (Menggunakan '@staticmethod') ---
    
    # Static Method: Fungsi utilitas independen untuk memvalidasi format email kantor
    @staticmethod
    def validasi_email_kantor(email):
        domain_kantor = "@perusahaan.com"
        if email.endswith(domain_kantor) and len(email) > len(domain_kantor):
            return f"Email '{email}' VALID untuk domain perusahaan."
        return f"Email '{email}' TIDAK VALID! Harus menggunakan domain {domain_kantor}."


# ==========================================
# INSTANSIASI DAN PENGUJIAN
# ==========================================

if __name__ == "__main__":
    # 1. Membuat minimal 2 Object dari Class Karyawan
    karyawan1 = Karyawan("Budi Santoso", "Software Engineer", 8000000)
    karyawan2 = Karyawan("Siti Rahma", "Data Analyst", 7500000)

    print("=== PENGUJIAN INSTANCE METHODS ===")
    # Pemanggilan Instance Method 1
    print(karyawan1.tampilkan_profil())
    print(karyawan2.tampilkan_profil())
    print()

    # Pemanggilan Instance Method 2
    print(karyawan1.hitung_total_gaji(10))  # Bonus 10%
    print(karyawan2.hitung_total_gaji(15))  # Bonus 15%
    print()

    print("=== PENGUJIAN STATIC METHOD ===")
    # Panggil Static Method melalui Nama Class
    email_test1 = "budi.santoso@perusahaan.com"
    print("[Via Class ]: " + Karyawan.validasi_email_kantor(email_test1))

    # Panggil Static Method melalui Objek
    email_test2 = "siti.rahma@gmail.com"
    print("[Via Objek ]: " + karyawan2.validasi_email_kantor(email_test2))