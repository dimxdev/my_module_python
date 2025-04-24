judul = " NESTED LIST/ LIST BERSARANG "
print(judul.center(40, "="))

data_1 = [1, 2, 4]
data_2 = [6, 4, 7]
data_3 = [5, 8, 9]
data_2D = [data_1, data_2, data_3]
print(f"data 1\t= {data_1}")
print(f"data 2\t= {data_2}")
print(f"data 3\t= {data_3}")
print(f"data 2D\t= {data_2D} \n")

## contoh penggunaan 
peserta_1 = ["asep", 20, "laki-laki"]
peserta_2 = ["wini", 23, "perempuan"]
peserta_3 = ["tantin", 20, "laki-laki"]
list_peserta = [peserta_1, peserta_2, peserta_3]
for peserta in list_peserta :
    print(f"nama\t= {peserta[0]}")
    print(f"umur\t= {peserta[1]}")
    print(f"kelamin\t= {peserta[2]} \n")

for peserta in list_peserta :
    print(peserta)







