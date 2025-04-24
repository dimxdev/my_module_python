judul = " COPY LIST "
print(judul.center(30, "="))


a = ["ucup", "otong", "asep", "udin"]
print(f"a = {a}")
b = a  # pass in the reference (menduplikat semuanya, termasuk id juga)
print(f"b = {b} \n")

## coba mengubah kedua isi list
a[1] = "usep"
print(f"a = {a}")
print(f"b = {b} \n")

b.sort() # semua akan ikut ke sort juga
print(f"a = {a}")
print(f"b = {b} \n")

## check id ke dua list
print(f"id a = {hex(id(a))}")
print(f"id b = {hex(id(b))}\n")

## menduplikat list mengguankan copy
c = a.copy()
print(f"a = {a}")
print(f"b = {b}")
print(f"c = {c} \n")

c[0] = "bolot"
print(f"a = {a}")
print(f"b = {b}")
print(f"c = {c} \n")


print(f"id a = {hex(id(a))}")
print(f"id b = {hex(id(b))}")
print(f"id b = {hex(id(c))}\n")


