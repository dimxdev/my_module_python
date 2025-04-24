import os
os.system("cls")

judul = " FUNCTION "
print(judul.center(30, "="))


## membuat function
def cetak_helloworld() :
    print("hello world")

def selamatPagi() :
    nama = input("masukkan nama anda : ")
    print(f"hallo, selamat pagi {nama} yang ganteng")

selamatPagi()
cetak_helloworld()