# t11.py
# Latihan 1 - Membuat Class Hero

class Hero:
    # Constructor: otomatis dipanggil saat object dibuat
    def __init__(self, name, hp, attack_power):
        self.name = name              # Nama hero
        self.hp = hp                  # Health Point
        self.attack_power = attack_power  # Kekuatan serangan

    # Method untuk menampilkan informasi hero
    def info(self):
        print(f"Hero: {self.name} | HP: {self.hp} | Power: {self.attack_power}")


# ======================
# Main Program
# ======================

# Membuat object Hero
hero1 = Hero("Layla", 100, 15)
hero2 = Hero("Zilong", 120, 20)

# Menampilkan info awal
hero1.info()
hero2.info()

print("\n--- Update HP Hero ---")

# Mengubah HP hero1
hero1.hp = 500

# Mengecek HP setelah diubah
print(f"HP baru {hero1.name}: {hero1.hp}")