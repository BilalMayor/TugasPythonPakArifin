# t5.py
# Latihan 5 - Abstraction & Interface

from abc import ABC, abstractmethod

# ======================
# Abstract Class / Interface
# ======================
class GameUnit(ABC):

    @abstractmethod
    def serang(self, target):
        pass

    @abstractmethod
    def info(self):
        pass


# ======================
# Class Hero
# ======================
class Hero(GameUnit):
    def __init__(self, nama):
        self.nama = nama

    def serang(self, target):
        print(f"Hero {self.nama} menebas {target}!")

    def info(self):
        print(f"Saya adalah Hero: {self.nama}")


# ======================
# Class Monster
# ======================
class Monster(GameUnit):
    def __init__(self, jenis):
        self.jenis = jenis

    def serang(self, target):
        print(f"Monster {self.jenis} menggigit {target}!")

    def info(self):
        print(f"Saya adalah Monster: {self.jenis}")


# ======================
# Main Program
# ======================
h = Hero("Alucard")
m = Monster("Serigala")

h.info()
m.info()

h.serang("Monster")
m.serang("Hero")