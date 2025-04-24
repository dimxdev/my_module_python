judul = "FOR LOOP"
print(judul.center(30, "="))

"""
   for (kondisi) :
       (aksi)
"""

## for dengan list
angka_list = [2, 4, 5, 7, 10]
print(angka_list)
for i in angka_list :
    print(f"i = {i}")
print("\n")

## for dengan range
angka_range = range(7)
print(angka_range)
for i in angka_range :
    print(f"i = {i}")
print("\n")

angka_range = range(3,7)
print(angka_range)
for i in angka_range :
    print(f"i = {i}")
print("\n")

## for menggunakan string 
data = "dimas ganteng"
for i in data :
    print(i)