judul = " BREAK "
print(judul.center(30, "="))

## break berfungsi untuk menghentikan perulangan secara paksa

angka = 0
while angka < 5 :
    angka += 1
    print(f"angka ke-{angka}")
    if angka == 3 :
        break
print("program selesai \n")

data_int = int(input("hentikan perulangan pada angka ke : "))
angka = 0
while True :
    angka += 1
    print(f"angka ke-{angka}")
    if angka == data_int :
        break
print("program selesai \n")






