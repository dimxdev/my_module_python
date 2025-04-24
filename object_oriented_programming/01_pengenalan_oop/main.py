import os
os.system("cls")

print(f"{"DRAMA SINGKAT MOBILE LEJEN":^50}")
print("_"*50, "\n")

class Hero:
    # Constructor untuk inisialisasi atribut
    def __init__(self, nama, Nyawa, demage, defend):
        self.nama = nama
        self.Nyawa = Nyawa
        self.demage = demage
        self.defend = defend

    # Metode untuk menyerang
    def serang(self, target):
        print(f"{self.nama} menyerang {target.nama}!")
        damage = self.demage - target.defend
        if damage > 0:
            target.Nyawa -= damage
            print(f"{target.nama} menerima {damage} demage!")
        else:
            print(f"{self.nama}'s serangan tidak efektif.")

    # Metode untuk memeriksa status
    def status(self):
        return f"Nama: {self.nama}, nyawa: {self.Nyawa}, demage: {self.demage}, defend: {self.defend}"


# Membuat objek dari class Hero
hero1 = Hero("Miya", 100, 30, 10)
hero2 = Hero("Alucard", 80, 20, 5)

# Memeriksa status masing-masing hero
print(hero1.status())  # Output: Nama: Knight, Kesehatan: 100, demage: 30, defend: 10
print(hero2.status())  # Output: Nama: Goblin, Kesehatan: 80, demage: 20, defend: 5
print("-"*50, "\n")

# Hero1 menyerang Hero2
hero1.serang(hero2)
print("-"*50, "\n")

# Memeriksa status setelah serangan
print(hero1.status())  
print(hero2.status())
print("-"*50, "\n")
