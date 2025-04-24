judul = " LATIHAN  PERULANGAN "
print(judul.center(30, "="))

## 1. buat segitiga menggunakan for
count = 1
for i in range(7) :
    print("*"*count)
    count += 1
print("program selesai \n")

## buat segitiga menggunakan while
count = 1
while count <= 4 :
    print("*"*count)
    count += 1

count = 1
data_input = int(input("berapa baris segitiga yang di inginkan : "))
totalBintang = 0
while True :
    totalBintang += 1
    print("*"*count)
    count += 1
    if totalBintang == data_input :
        break
print("program selesai \n")

## buat segitiga ganjil nya saja
bintang = "*"
count = 1
while count < 10 :
    print((count*bintang).center(10))
    count +=2
bintang = "*"
count = 7
while count > 0 :
    print((count*bintang).center(10))
    count -=2
