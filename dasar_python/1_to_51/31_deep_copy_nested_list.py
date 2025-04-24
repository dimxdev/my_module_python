judul = " DEEPCOPY NESTED LIST  "
print(judul.center(30, "="))

data_1 = [1, 2, 3]
data_2 = [5, 7, 8]
data_2D = [data_1, data_2, 10]
data_2d_copy = data_2D.copy()
print(f"data 1 \t= {data_1}")
print(f"data 2 \t= {data_2}")
print(f"data 2d\t= {data_2D}")
print(f"data 2d copy = {data_2d_copy}\n")

## mengambil data dari nested list
data = data_2D[0][1]
print(f"data index [0][1] = {data}\n")

## adress semua data
print(f"adress data 2d\t\t= {hex(id(data_2D))} ")
print(f"adress data 2d copy\t= {hex(id(data_2d_copy))} \n")

print(f"adress data 2d [0]\t\t= {hex(id(data_2D[0]))} ")
print(f"adress data 2d copy[0]\t= {hex(id(data_2d_copy[0]))}\n")

## merubah isi salah satu list
data_2d_copy[0][1] = 10 
data_2D [2] = 7
print(f"data 2d\t= {data_2D}")
print(f"data 2d copy = {data_2d_copy}\n")

## menggunakan deepcopy
from copy import deepcopy

data_2D = [data_1, data_2, 10]
data_2D_deepcopy = deepcopy(data_2D)
print(f"data 2d\t\t= {data_2D}")
print(f"data 2d deepcopy= {data_2D_deepcopy}\n")

print(f"adress data 2d\t\t= {hex(id(data_2D))} ")
print(f"adress data 2d deepcopy\t= {hex(id(data_2d_copy))} \n")

print(f"adress data 2d [0]\t\t= {hex(id(data_2D[0]))} ")
print(f"adress data 2d deepcopy[0]\t= {hex(id(data_2D_deepcopy[0]))}\n")

## merupah isi data salah satu list
data_2D_deepcopy [0][1] = 11
data_2D[1][2] = 99
print(f"data 2d\t\t= {data_2D}")
print(f"data 2d deepcopy= {data_2D_deepcopy}\n")



