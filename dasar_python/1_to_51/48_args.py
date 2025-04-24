import os
os.system("cls")

print(f"{" *ARGS ":^20}")
print("-"*20)


## memasukkan argument pada umumnya
def data_diri(nama, tinggi, berat) :
    print(f"nama = {nama}\ntinggi = {tinggi} cm\nberat = {berat} kg\n")
data_diri("dimas", 180, 45)

def data_lis(data_list) :
    data = data_list.copy()
    nama = data[0]
    tinggi = data[1]
    berat = data[2]
    print(f"{nama} mempunyai tinggi {tinggi}cm serta berat {berat}kg\n")
nama = input("nama = ")
tinggi = int(input("tinggi = "))
berat = int(input("berat = "))
data_lis([nama, tinggi, berat])


## argument menggunakan args (*) {memasukkan argument sesuka kita berapa pun jumlahnya}
def data_lis2(*lis) :
    nama = lis[0]
    tinggi = lis[1]
    berat = lis[2]
    print(f"{nama} mempunyai tinggi {tinggi}cm serta berat {berat}kg\n")
data_lis2("dudung", 23, 35)

def tambah(*data) :
    a = 0
    for b in data :
        a += b
    return a
p1 = tambah(3,4,5,6)
print(p1)
p2 = tambah(3,4,5,6,56,43,23,4,5)
print(p2)
