import os 
os.system("cls")

judul = " FUNCTION WITH ARGUMENT "
print(judul.center(30, "="))

## argument string
def hello_world(nama) :
    print(f"selamat pagi {nama} ganteng")
hello_world("DIMAS")
print("program selesai \n")


## argument integer
def tambah(angka_1, angka_2) :
    hasil = angka_1 + angka_2
    print(f"{angka_1} + {angka_2} = {hasil} ")
tambah(89, 77)
tambah("halo", "bro")
print("program selesai \n")


## argument list
def say_hi(list_peserta) :
    data_peserta = list_peserta.copy() ## pakai copy supaya ketika ketika ingin merubah isi listnya, list aslinya tidak akan berubah
    data_peserta[2] = "putra"
    for peserta in data_peserta :
        print(f"hi {peserta} ganteng")
kelas_C = ["asep", "ucup", "otong"]
say_hi(kelas_C)
print("program selesai \n")




































