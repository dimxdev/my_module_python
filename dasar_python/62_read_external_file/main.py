import os 
os.system("cls")
print(f"{'READ EXTERNAL FILE':^30}")
print("_"*30, "\n")


## MEMBACA FILE
file = open("data.txt", mode="r")

## CHECK STATUS
print(f"status read = {file.readable()}")
print(f"status write = {file.writable()}")
print("-"*30, "\n")

   # MEMBACA SELURUH FILE
print(file.read())
print("-"*30, "\n")

   # MEMBACA PERBARIS
# print(file.readline()) # baca baris pertama
# print(file.readline(), end="") # baca baris kedua
# print(file.readline()) # baca baris ketiga

   # MEMBACA SEMUA BARIS SEBAGAI LIST
# print(file.readlines())

## HARUS DI CLOSE SETELAH MEMBUKA FILE
print(f"apakah file sudah di close = {file.closed}")
file.close()
print(f"apakah file sudah di close = {file.closed}")
print("-"*30, "\n\n")



## CARA LAIN MEMBACA FILE
with open("data.txt", mode="r") as filee : # (dengan saat file ini dibuka, apa yg ingin dilakukan)
    content = filee.read()
    print(content)
    print(f"apakah file sudah di close = {filee.closed}")
print(f"apakah file sudah di close = {filee.closed}")  
print("-"*30, "\n\n")


