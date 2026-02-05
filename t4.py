# t4.py
# Latihan 4 - Encapsulation (Mengamankan Data HP)

class Hero:
    def __init__(self, nama, hp_awal):
        self.nama = nama
        self.__hp = hp_awal  # PRIVATE ATTRIBUTE

    # GETTER
    def get_hp(self):
        return self.__hp

    # SETTER dengan validasi
    def set_hp(self, nilai_baru):
        if nilai_baru < 0:
            self.__hp = 0
        elif nilai_baru > 1000:
            print("Cheat terdeteksi! HP dibatasi ke 1000.")
            self.__hp = 1000
        else:
            self.__hp = nilai_baru

    def diserang(self, damage):
        sisa_hp = self.get_hp() - damage
        self.set_hp(sisa_hp)
        print(f"{self.nama} terkena damage {damage}. Sisa HP: {self.get_hp()}")


# ======================
# Uji Coba
# ======================

hero1 = Hero("Layla", 100)

print("--- UJI SETTER ---")
hero1.set_hp(-50)
print("HP sekarang:", hero1.get_hp())

hero1.set_hp(2000)
print("HP sekarang:", hero1.get_hp())

print("\n--- UJI DISERANG ---")
hero1.diserang(200)

print("\n--- UJI NAME MANGLING ---")
print("Akses paksa HP:", hero1._Hero__hp)