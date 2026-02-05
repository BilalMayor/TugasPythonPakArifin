# techmaster.py
# Proyek Integrasi OOP - TechMaster

from abc import ABC, abstractmethod

# ==================================================
# ABSTRACT CLASS
# ==================================================
class BarangElektronik(ABC):
    def __init__(self, nama, harga_dasar):
        self.nama = nama
        self.__stok = 0
        self.__harga_dasar = harga_dasar

    # GETTER
    def get_stok(self):
        return self.__stok

    def get_harga_dasar(self):
        return self.__harga_dasar

    # SETTER STOK DENGAN VALIDASI
    def tambah_stok(self, jumlah):
        if jumlah < 0:
            print(f"Gagal update stok {self.nama}! Stok tidak boleh negatif ({jumlah}).")
        else:
            self.__stok += jumlah
            print(f"Berhasil menambahkan stok {self.nama}: {jumlah} unit.")

    @abstractmethod
    def tampilkan_detail(self):
        pass

    @abstractmethod
    def hitung_harga_total(self, jumlah):
        pass


# ==================================================
# CLASS LAPTOP
# ==================================================
class Laptop(BarangElektronik):
    def __init__(self, nama, harga_dasar, processor):
        super().__init__(nama, harga_dasar)
        self.processor = processor

    def tampilkan_detail(self):
        print(f"[LAPTOP] {self.nama} | Proc: {self.processor}")

    def hitung_harga_total(self, jumlah):
        pajak = 0.10 * self.get_harga_dasar()
        return (self.get_harga_dasar() + pajak) * jumlah


# ==================================================
# CLASS SMARTPHONE
# ==================================================
class Smartphone(BarangElektronik):
    def __init__(self, nama, harga_dasar, kamera):
        super().__init__(nama, harga_dasar)
        self.kamera = kamera

    def tampilkan_detail(self):
        print(f"[SMARTPHONE] {self.nama} | Cam: {self.kamera}")

    def hitung_harga_total(self, jumlah):
        pajak = 0.05 * self.get_harga_dasar()
        return (self.get_harga_dasar() + pajak) * jumlah


# ==================================================
# POLYMORPHISM FUNCTION
# ==================================================
def proses_transaksi(daftar_belanja):
    print("\n--- STRUK TRANSAKSI ---")
    total = 0

    for i, (barang, jumlah) in enumerate(daftar_belanja, start=1):
        barang.tampilkan_detail()
        subtotal = barang.hitung_harga_total(jumlah)
        print(f"   Beli: {jumlah} unit | Subtotal: Rp {int(subtotal):,}\n")
        total += subtotal

    print("----------------------------------------")
    print(f"TOTAL TAGIHAN: Rp {int(total):,}")
    print("----------------------------------------")


# ==================================================
# MAIN PROGRAM
# ==================================================
print("--- SETUP DATA ---")

laptop1 = Laptop("ROG Zephyrus", 20_000_000, "Ryzen 9")
hp1 = Smartphone("iPhone 13", 15_000_000, "12MP")

laptop1.tambah_stok(10)
hp1.tambah_stok(-5)
hp1.tambah_stok(20)

keranjang = [
    (laptop1, 2),
    (hp1, 1)
]

proses_transaksi(keranjang)