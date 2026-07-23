# Pertemuan_5/main.py

class DompetDigital:
    def __init__(self, id_pengguna, pin, saldo_awal):
        # 1. MINIMAL 3 PRIVATE ATTRIBUTES (Gunakan awalan __)
        self.__id_pengguna = id_pengguna
        self.__pin = pin
        self.__saldo = saldo_awal

    # 2. METODE GETTER (Akses data privat secara aman)
    def get_id_pengguna(self):
        return self.__id_pengguna

    # 3. METODE VALIDASI (Perlu verifikasi PIN sebelum data diakses / dimodifikasi)
    def cek_saldo(self, input_pin):
        """Memeriksa saldo dengan memverifikasi PIN terlebih dahulu."""
        if input_pin == self.__pin:
            return f"[Akses Diterima] Saldo Anda saat ini: Rp{self.__saldo:,}"
        else:
            return "[Akses Ditolak] PIN yang Anda masukkan SALAH!"

    def isi_saldo(self, input_pin, jumlah):
        """Menambah saldo jika PIN benar dan nominal valid."""
        if input_pin != self.__pin:
            return "[Akses Ditolak] Transaksi gagal, PIN SALAH!"
        
        if jumlah <= 0:
            return "[Gagal] Nominal isi saldo harus lebih dari 0!"

        self.__saldo += jumlah
        return f"[Berhasil] Top-up Rp{jumlah:,} berhasil! Saldo baru: Rp{self.__saldo:,}"

    def tarik_tunai(self, input_pin, jumlah):
        """Mencairkan/menarik saldo dengan validasi PIN dan kecukupan saldo."""
        if input_pin != self.__pin:
            return "[Akses Ditolak] Transaksi gagal, PIN SALAH!"

        if jumlah > self.__saldo:
            return "[Gagal] Saldo tidak mencukupi untuk melakukan penarikan ini!"

        self.__saldo -= jumlah
        return f"[Berhasil] Penarikan Rp{jumlah:,} berhasil! Sisa saldo: Rp{self.__saldo:,}"


# ==========================================
# INSTANSIASI DAN PENGUJIAN
# ==========================================

if __name__ == "__main__":
    print("=== 1. INSTANSIASI OBJEK ===")
    # Memilih 1 Object dari Class DompetDigital
    dompet_user = DompetDigital(id_pengguna="USER12345", pin="12345", saldo_awal=500000)
    
    # Pengujian Getter untuk ID Pengguna (yang bersifat aman)
    print(f"ID Pengguna: {dompet_user.get_id_pengguna()}")
    print()

    print("=== 2. PEMBUKTIAN PRIVATE ATTRIBUTE (AKSES LANGSUNG) ===")
    # Mengakses atribut privat secara langsung akan menghasilkan AttributeError:
    # print(dompet_user.__saldo)  # ERROR! AttributeError: 'DompetDigital' object has no attribute '__saldo'
    # print(dompet_user.__pin)    # ERROR! AttributeError: 'DompetDigital' object has no attribute '__pin'
    print("Atribut __saldo dan __pin tidak dapat diakses langsung dari luar kelas (Terlindungi oleh Encapsulation).")
    print()

    print("=== 3. PENGUJIAN METODE VALIDASI (VERIFIKASI PIN) ===")
    
    print("\n--- A. Pengecekan Saldo ---")
    print("Mencoba PIN Salah :", dompet_user.cek_saldo("000000"))
    print("Mencoba PIN Benar :", dompet_user.cek_saldo("123456"))

    print("\n--- B. Penambahan Saldo (Isi Saldo) ---")
    print("Mencoba PIN Salah :", dompet_user.isi_saldo("111111", 100000))
    print("Mencoba PIN Benar :", dompet_user.isi_saldo("123456", 200000))

    print("\n--- C. Penarikan Tunai ---")
    print("Mencoba Saldo Tidak Cukup :", dompet_user.tarik_tunai("123456", 1000000))
    print("Mencoba PIN Benar & Saldo Cukup :", dompet_user.tarik_tunai("123456", 150000))