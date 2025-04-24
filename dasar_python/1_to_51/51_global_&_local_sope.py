import os
os.system("cls")

print(f"{"GLOBAL & LOCAL SCOPE":^30}")
print("_"*30, "\n")


## Global scope
nama_global = "DIMAS"

   # akses menggunakan fungsi
def say_hi() :
    print(f"halo {nama_global}")
say_hi()
print("-"*20, "\n")

   # akses menggunakan loop
for i in range(1,6) :
    print(f"{i} - {nama_global}")
print("-"*20, "\n")

   # akses menggunakan percabangan 
if True :
    print(f"if menampilkan {nama_global}")
print("-"*20, "\n")

   # contoh penggunaan 1
def halo_global() :
    print(f"hallo {nama_global}")
halo_global()
print("-"*20, "\n")

   # contoh penggunaan 2 (merubah global scope menggunakan function)
angka = 0
nama = "dudung"
def ubah(angka_baru, nama_baru) :
    global angka
    global nama
    angka = angka_baru
    nama = nama_baru
print(f"sebelum = ({angka}, {nama})")
ubah(4, "asep")
print(f"sesudah = ({angka}, {nama})")
print("-"*20, "\n")

   # contoh penggunaan 3 (merubah global scope menggunakan loop dan kondisi) 
angka = 0
for i in range(1,6) :
    angka += i
    angka_dummy = 0
print(f"angka = {angka}")
print(f"angka dummy = {angka_dummy}")

if True :
    angka = 50
    angka_dummy = 30
print(f"angka = {angka}")
print(f"angka dummy = {angka_dummy}")
print("-"*20, "\n")


## Local scope
def fungsi() :
    nama_local = "asep"
    return print(nama_local)
fungsi()
print("-"*20, "\n")
# print(nama_local) --> tidak bisa

