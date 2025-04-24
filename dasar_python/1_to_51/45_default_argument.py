import os
os.system("cls")

judul = " DEFAULT ARGUMENT "
print(judul.center(30, "="))


# satu asignment
def hello(nama = "ganteng"):
    print(f"selamat pagi {nama}")
hello("dimas")
print("next \n")


# 2 asigment
def sapa(nama, sapa = "selamat pagi") :
    print(f"halo {nama}, {sapa}")
sapa("ganteng")
sapa("dimas","pagi")
sapa("", "pagi")
print("next \n")


# contoh lagi
def pangkat(angka, pangkat = 2) :
    hasil = angka**pangkat
    return hasil
print(pangkat(2,8))
a = pangkat(angka = 2, pangkat = 3)
print(a)
b = pangkat(angka = 4, pangkat = 4)
print(b)
print("next \n")

def tambah(ang1 = 1, ang2 = 2, ang3 = 4, ang4 = 8) :
    hasil = ang1 + ang2 + ang3 + ang4
    return hasil
print(tambah())
print(tambah(ang3= 3, ang1 = 4, ang4 = 7))
