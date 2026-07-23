"""
Tugas Pertemuan 8 - Exception Handling & Custom Exception
File: exception_handling_lab.py
"""

# ===================================================
# 1. Custom Exception Class
# ===================================================
class SaldoTidaktercukupiError(Exception):
    """Exception khusus jika saldo tidak mencukupi untuk transaksi."""
    def __init__(self, saldo_saat_ini, jumlah_tarik):
        self.saldo_saat_ini = saldo_saat_ini
        self.jumlah_tarik = jumlah_tarik
        message = (
            f"Penarikan sebesar Rp{jumlah_tarik:,} gagal! "
            f"Saldo saat ini hanya Rp{saldo_saat_ini:,}."
        )
        super().__init__(message)


class InputJumlahTidakValidError(Exception):
    """Exception khusus jika jumlah transaksi bernilai 0 atau negatif."""
    def __init__(self, jumlah):
        self.jumlah = jumlah
        message = f"Jumlah transaksi harus lebih dari 0! Input diberikan: {jumlah}"
        super().__init__(message)


# ===================================================
# 2. Class Utama (Logika Bisnis)
# ===================================================
class RekeningBank:
    def __init__(self, nomor_rekening, pemegang_rekening, saldo_awal=0):
        self.nomor_rekening = nomor_rekening
        self.pemegang_rekening = pemegang_rekening
        self.saldo = saldo_awal

    def tarik_tunai(self, jumlah):
        # Validasi 1: Input harus lebih dari 0
        if jumlah <= 0:
            raise InputJumlahTidakValidError(jumlah)

        # Validasi 2: Saldo harus mencukupi
        if jumlah > self.saldo:
            raise SaldoTidaktercukupiError(self.saldo, jumlah)

        self.saldo -= jumlah
        print(f"Penarikan Rp{jumlah:,} berhasil. Sisa saldo: Rp{self.saldo:,}")
        return self.saldo


# ===================================================
# 3. Implementasi Try-Except-Finally & Main Execution
# ===================================================
if __name__ == "__main__":
    rekening = RekeningBank("123456789", "Naufal", saldo_awal=500_000)

    # Uji Coba 1: Penarikan Berhasil
    print("--- Skenario 1: Penarikan Valid ---")
    try:
        rekening.tarik_tunai(200_000)
    except (SaldoTidaktercukupiError, InputJumlahTidakValidError) as e:
        print(f"[ERROR]: {e}")
    finally:
        print("[FINALLY]: Proses pemeriksaan Skenario 1 selesai.\n")

    # Uji Coba 2: Saldo Tidak Mencukupi (Memicu Custom Exception)
    print("--- Skenario 2: Penarikan Melebihi Saldo ---")
    try:
        rekening.tarik_tunai(400_000)
    except SaldoTidaktercukupiError as e:
        print(f"[CUSTOM ERROR DETECTED]: {e}")
    except InputJumlahTidakValidError as e:
        print(f"[ERROR]: {e}")
    finally:
        print("[FINALLY]: Proses pemeriksaan Skenario 2 selesai.\n")

    # Uji Coba 3: Input Negatif (Memicu Custom Exception)
    print("--- Skenario 3: Input Tidak Valid ---")
    try:
        rekening.tarik_tunai(-50_000)
    except (SaldoTidaktercukupiError, InputJumlahTidakValidError) as e:
        print(f"[CUSTOM ERROR DETECTED]: {e}")
    finally:
        print("[FINALLY]: Proses pemeriksaan Skenario 3 selesai.")