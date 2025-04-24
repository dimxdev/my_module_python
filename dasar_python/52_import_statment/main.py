import os
os.system("cls")

print(f"{"IMPORT STATMENT":^30}")
print("_"*30, "\n")


## 1. menyambung program dari file external
import print1
import print2
print("-"*20, "\n")


## 2. import dengan variabel
import variabel1 as v1
import variabel2 as v2

print(v1.data)
print(v2.data)
print("-"*20, "\n")


## 3. import dengan fungsi
import matematika

print(f"hasil tambah \t= {matematika.tambah(3, 5)}")
print(f"hasil kali \t= {matematika.kali(3, 5)}")
print("-"*20, "\n")
