## 1. MODE WRITE (DIA AKAN MEMBUAT FILE BARU JIKA BELOM ADA, LALU AKAN MERUBAH SEMUA ISINYA)
with open("data1.txt", "w", encoding="utf-8") as file:
    file.write("jhon si jhony")

with open("data1.txt", "w", encoding="utf-8") as file:
    file.write("otong su rotong")

with open("data1.txt", "w", encoding="utf-8") as file:
    file.write("asep")


## 2. MODE APPEND
with open("data2.txt", "w", encoding="utf-8") as file:
    file.write("jhon si jhony\n")

with open("data2.txt", "a", encoding="utf-8") as file:
    file.write("jhun si jhony\n")

with open("data2.txt", "a", encoding="utf-8") as file:
    file.write("jhun si jhony\n")


## 3. MODE R+
with open("data3.txt", "w", encoding="utf-8") as file:
    file.write("data ke-3\n")

with open("data3.txt", "r+", encoding="utf-8") as file:
    file.write("baris-1\n")
    file.write("baris-2\n")
    file.write("baris-3\n")

with open("data3.txt", "r+", encoding="utf-8") as file:
    baca = file.read()
    print(baca)

with open("data3.txt", "r+", encoding="utf-8") as file:
    file.write("otong") # akan menimpa isi tkt sesuai dengan panjang data