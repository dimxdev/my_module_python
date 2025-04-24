judul = " MULTI KEYS & NESTING DICTIONARY "
print(judul.center(60, "="), "\n")

import datetime as dt

mahasiswa1 = {
    "nim" : "2350082081",
    "nama" : "Dimas",
    "total_sks" : 120,
    "beasiswa" : False,
    "lahir" : dt.datetime(2006, 1, 15)
}

mahasiswa2 = {
    "nim" : "2350082082",
    "nama" : "Tuntin",
    "total_sks" : 120,
    "beasiswa" : True,
    "lahir" : dt.datetime(2005, 7, 10)
}

mahasiswa3 = {
    "nim" : "2350082083",
    "nama" : "Sopi",
    "total_sks" : 120,
    "beasiswa" : False,
    "lahir" : dt.datetime(2004, 4, 19)
}

data_mahasiswa = {
    "MAH001" : mahasiswa1,
    "MAH002" : mahasiswa2,
    "MAH003" : mahasiswa3,
}

print("="*54)
print(f"{"KEY":<6} {"NIM":<11} {"NAMA":<10} {"SKS":<4} {"BEASISWA":<9} {"TGL_LAHIR":<10}")
print("="*54)
for mahasiswa in data_mahasiswa :
    KEY = mahasiswa
    NIM = data_mahasiswa[KEY]["nim"]
    NAMA = data_mahasiswa[KEY]["nama"]
    TOTAL_SKS = data_mahasiswa[KEY]["total_sks"]
    BEASISWA = data_mahasiswa[KEY]["beasiswa"]
    TGL_LAHIR = data_mahasiswa[KEY]["lahir"].strftime("%d/%m/%y")
    print(f"{KEY:<6} {NIM:<11} {NAMA:<10} {TOTAL_SKS:<4} {BEASISWA:^10} {TGL_LAHIR:<10}")
    # print("-"*54)
print("="*54, "\n")



