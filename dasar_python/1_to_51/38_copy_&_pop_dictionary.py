judul = " COPY DICTIONARY "
print(judul.center(30, "="))


data_mahasiswa = {
    "let" : "silet",
    "gok" : "dlogok",
    "mbut" : "jwembut",
    "sok" : "bosok",
}


## copy dictionary
data_student = data_mahasiswa.copy()
print(f"data mahasiswa = {data_mahasiswa}")
print(f"data mahasiswa2 = {data_student} \n")

data_mahasiswa['let'] = "siliets" ## coba dirubah isi salah satu
print(f"data mahasiswa = {data_mahasiswa}")
print(f"data mahasiswa2 = {data_student} \n")


## pop dictionary (memindahkan data ke tempat lain berdasarkan key)
data_siliets = data_mahasiswa.pop("let")
print(f"data let = {data_siliets}")
print(f"data mahasiswa = {data_mahasiswa}")
print(f"data mahasiswa2 = {data_student} \n")


## popitem dictionary (memindahkan data ke tempat lain berdasarkan key yang terakhir)
data_terakhir = data_mahasiswa.popitem()
print(f"data terakhir = {data_terakhir}")
print(f"data mahasiswa = {data_mahasiswa}")
print(f"data mahasiswa2 = {data_student} \n")

data_gabungan = [data_siliets, data_terakhir]
print(data_gabungan)
