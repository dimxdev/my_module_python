judul = " LOOPING DICTIONARY "
print(judul.center(30, "="))

data_mahasiswa = {
    "cup" : "ucup",
    "tong" : "entong",
    "su" : "asu",
    "let" : "silet", 
}

## looping biasa (yang keluar cuma keynya)
for mahasiswa in data_mahasiswa :
    print(mahasiswa)
print("program selesai \n")

## operator untuk mengambil key 
keys = data_mahasiswa.keys()
print(keys)
for key in keys : ## penulisan 1
    print(data_mahasiswa.get(key)) 
keys = data_mahasiswa.keys()
print(keys)
for key in data_mahasiswa.keys() :  ## penulisan 2
    print(data_mahasiswa.get(key)) 
print("program selesai \n")


## operator untuk mengambil values 
values = data_mahasiswa.values()
print(values)
for value in values :
    print(value)
print("program selesai \n")


## operator untuk mengambil items (key dan value)
items = data_mahasiswa.items()
print(items)
for item in items :
    print(item)
for key, value in items :
    print(f"key = {key}, value = {value}")
print("program selesai \n")



