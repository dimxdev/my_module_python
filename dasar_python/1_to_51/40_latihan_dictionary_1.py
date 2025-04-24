import datetime as dt
import os

judul = " LATIHAN DICTIONARY 1 "
os.system("cls")
print(judul.center(40,"="))


mahasiswa_template = {
    "nama" : None,
    "nim" : None,
    "sks lulus" : None,
    "lahir" : None
}
print(mahasiswa_template)

print("="*30)
print(" DATA MAHASISWA ".center(30))
print("="*30)

mahasiswa = dict.fromkeys(mahasiswa_template.keys(), "kosong")
print(mahasiswa)
mahasiswa ["nama"] = input("Nama mahasiswa : ")
mahasiswa ["nim"] = input("Nim mahasiswa : ")
mahasiswa ["sks lulus"] = input("total SKS : ")
TAHUN_LAHIR = int(input("tahun lahir (yyyy) : "))
BULAN_LAHIR = int(input("bukan lahir (mm) : "))
TANGGAL_LAHIR = int(input("tgl lahir (dd) : "))
mahasiswa ["lahir"] =dt.datetime(TAHUN_LAHIR, BULAN_LAHIR, TANGGAL_LAHIR).strftime("%d/%m/%Y")
print(mahasiswa)


