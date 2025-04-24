judul = " MANIPULASI LIST "
print(judul.center(30, "="))

import random

## index  0(-4),  1(-3),  2(-2),  3(-1)  
data = ["asep", "ucup", "dadang", "dudung"]

## mengambil data list
data_0 = data[0]
print(data_0)

data_terakhir = data[-1]
print(data_terakhir)

data_acak = random.choice(data)
print(data_acak)

## mengambil info jumlah data dalam list
jumlah_data = len(data)
print(jumlah_data)

## merubah data 
print(data)
data[2] = "witot"
print(data)

## memanipulasi list
   # menambahkan data sesuai posisi
print(f"data = {data}")
data.insert(2, "dimas")
print(f"data = {data}")

   # menambah di akhir list 
data.append("usup")
print(f"data = {data}")

   # menambah list dengan list
data_baru = ["ujang", "kimaq"]
data.extend(data_baru)
print(f"data = {data}")

## me remove data dalam list
data.remove(data[0])
print(f"data = {data}")
data.remove("kimaq")
print(f"data = {data}")

   # meremove untuk di akhir
data.pop()
print(f"data = {data}")
   
   # meremove semua
data.clear()
print(f"data = {data}")

print("program selesai \n")




