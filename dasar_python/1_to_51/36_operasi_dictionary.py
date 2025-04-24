judul = " OPERAI DICTIONARY "
print(judul.center(30, "="))

data_dict = {
    'cup' : 'ucup',
    'sep' : 'asep',
    'dung' : 'dudung',
}

## panjang dictionary
PANJANG_DICT = len(data_dict)
print(f"panjang dictionary = {PANJANG_DICT}")


## mengecek key ada atau tidak
KEY = "cup"
CHECK_KEY = KEY in data_dict
print(f"apakah {KEY} ada dalam dictionary = {CHECK_KEY}")


## mengankses value (read) dengan get
print(data_dict['sep']) # cara umum
print(data_dict.get('cup')) # cara khusus
print(data_dict.get('cep', 'key tidak ditemukan')) # bisa di isi dengan keterangan jika key nya tidak ada


## mengupdate data 
data_dict['cup'] = "usep" # cara umum mengganti
print(data_dict)
data_dict['cep'] = "cecep" # cara umum menambah
print(data_dict)

data_dict.update({'cup' : 'ucup'}) # cara khusus mengganti
print(data_dict)
data_dict.update({'gok' : 'ndlogok'}) # cara khusus menambah
print(data_dict)


## menghapus data
del data_dict['gok']
print(data_dict)


print("program selesai\n")
