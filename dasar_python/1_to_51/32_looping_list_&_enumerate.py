judul = " LOOPING LIST DAN ENUMERATE "
print(judul.center(40, "="))

## menggunakan for loop
kumpulan_angka = [1,3,5,6,8,90]
for angka in kumpulan_angka :
    print(f"angka = {angka**2}")
print("program selesai\n")

kumpulan_peserta = ["otong","ucup","asep","dudung"]
for peserta in kumpulan_peserta :
    print(f"peserta = {peserta}")
print("program selesai\n")


## menggunakan for loop dan range 
kumpulan_angka = [1,3,5,6,8,90]
total_data = len(kumpulan_angka)
for angka in range(total_data) :
    print(f"angka = {kumpulan_angka[angka]}") 
print("program selesai\n")


## menggunakan while
kumpulan_angka = [1,3,5,6,8,90]
total_data = len(kumpulan_angka)
angka = 0
while angka < total_data :
    print(f"angka = {kumpulan_angka[angka]}")
    angka += 1
print("program selesai\n")


## list comprehension
kumpulan_angka = [1,3,5,6,8,90]
[print(f"data = {data}") for data in kumpulan_angka]
print("program selesai\n")
# comp = [data for data in kumpulan_angka]
# print(comp)

   # fungsi lain list comprehension
angka = [1, 2, 3, 4, 5, 6]
angka_genap = [x for x in angka if x % 2 == 0]
print(angka_genap)
angka = [1, 2, 3, 4, 5]
hasil = [x * 2 for x in angka]
print(hasil)
print("program selesai\n")


## enumerate 
angka = [1, 2, 3, 4, 5, 6]
for index,data in enumerate(angka):
    print(f"index = {index}, data = {data}")
print("program selesai\n")

