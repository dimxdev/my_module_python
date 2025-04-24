from math import nan


# ## contoh 1
# input_user = int(input("masukkan angka pembagi 10 : "))
# hasil = nan
# try:
#     hasil = 10/input_user
# except:
#     print("input tidak boleh 0")
# print(f"hasil = {hasil}")


## contoh 2 (jika sudah error dibaris pertama, maka baris yang lain akan di skip)
while(True):
    angka = int(input("masukkan angka pembagi 10 : "))
    try:
        hasil = 10/angka
        print(f"hasil = {hasil}")
        is_done = input("apakah lanjut (y/n) : ")
        if is_done == "n":
            break
    except:
        print("pembagi 0, masukkan input lain")
print("program selesai")
