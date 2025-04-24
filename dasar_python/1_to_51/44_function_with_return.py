import os
os.system("cls")

judul = " FUNGSI DENGAN RETURN "
print(judul.center(30, "="))

"""
   fungsi dengan return itu bisa mengembaklikan nilai atau 
   fungsi bisa disimpan kedalam variabel 
"""


## fungsi kuadrat
print("="*15)
print("FUNGSI KUADRAT")
print("="*15)

def kuadrat(angka) :
    operasi = angka**2
    return operasi**2

a = kuadrat(2)
print(a)
b = 10 + a
print(b)
c = 10 + kuadrat(3)
print(c) 
print(kuadrat(9))
print("program selesai \n")


## fungsi tambah
print("="*15)
print("FUNGSI TAMBAH")
print("="*15)

def tambah(angka1, angka2) :
    return angka1 + angka2

a = tambah(3, 5)
print(a)
print("program selesai \n")


## fungsi dengan return banyak
print("="*29)
print("FUNGSI DENGAN RETURN BANYAK")
print("="*29)

   #menggunakan return
def kalkulator(angka1, angka2) :
    tambah = angka1 + angka2
    kurang = angka1 - angka2
    kali = angka1 * angka2
    bagi = angka1 / angka2

    return tambah, kurang, kali, bagi

# jika ingin dipisah pisah
a = int(input("masukkan angka pertama : "))
b = int(input("masukkan angka kedua : "))
tambah, kurang, kali, bagi = kalkulator(a, b)
print(f"hasil operasi {a} & {b} = ")
print(f"hasil tambah = {tambah}")
print(f"hasil kurang = {kurang}")
print(f"hasil kali = {kali}")
print(f"hasil bagi = {bagi}")

# jika ingin disatukan dan akan membentuk tuple
hm = kalkulator(2,4)
print(hm)
print(hm[0])
print("program selesai \n")

   # tidak menggunakan return
def kalkulator2(angka1, angka2) :
    tambah = angka1 + angka2
    kurang = angka1 - angka2
    kali = angka1 * angka2
    bagi = angka1 / angka2

    print(f"hasil tambah = {tambah}")
    print(f"hasil kurang = {kurang}")
    print(f"hasil kali = {kali}")
    print(f"hasil bagi = {bagi}")

a = int(input("masukkan angka pertama : "))
b = int(input("masukkan angka kedua : "))
kalkulator2(a,b)
print("program selesai \n")


