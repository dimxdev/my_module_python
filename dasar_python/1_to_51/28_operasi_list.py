judul = " OPERASI LIST "
print(judul.center(30, "="))


## count data 
list_angka = [1, 2, 5, 8, 9, 10, 3, 4, 3, 6, 7, 5, 6, 5]
print(list_angka)
data_3 = list_angka.count(3)
data_5 = list_angka.count(5)
print(f"angka tiga sebanyak = {data_3}")
print(f"angka lima sebanyak = {data_5} \n")

## ambil posisi data (index)
list_nama = ["asep", "ucup", "dadang", "dudung"]
print(list_nama)
index_asep = list_nama.index("asep")
print(f"asep berada pada index = {index_asep} \n")

## mengurutkan data
list_angka = [1, 2, 5, 8, 9, 10, 3, 4, 3, 6, 7, 5, 6, 5]
print(list_angka)
list_angka.sort()
print(list_angka)

## membalikkan urutan
list_angka.reverse()
print(list_angka)

print("program selesai \n")


