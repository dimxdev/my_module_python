import os
os.system("cls")

print(f"{"LAMBDA & ANONYMOUS FUNCTION":^40}")
print("-"*40)


## FUNCTION
   # normal
def kuadrat1(angka) :
    return angka**2
print(f"hasil kuadrat menggunakan normal function = {kuadrat1(4)}")

   # lambda
kuadrat2 = lambda angka : angka**2
print(f"hasil kuadrat menggunakan lambda function = {kuadrat2(3)}")

kuadrat3 = lambda angka, pangkat : angka**pangkat
print(f"hasil kuadrat menggunakan lambda function = {kuadrat3(2,3)} \n")


## sorting
   # sorting list (biasa)
data_list1 = ["ucup", "otong", "asep"]
print(f"data list = {data_list1}")
data_list1.sort()
print(f"hasil normal sort = {data_list1}")

   # sorting menggunakan function
def panjang_nama(data) :
    return len(data)
data_list2 = ["ucup", "otong", "asep"]
# data_list2.sort(key = len)
data_list2.sort(key=panjang_nama)
print(f"hasil function panjang_nama sort = {data_list2}")
   
   # sorting list (lambda)
data_list3 = ["ucup", "otong", "asep"]
data_list3.sort(key= lambda data : len(data))
print(f"hasil lambda sort = {data_list3} \n")


## filter
   # menggunakan function
data_angka = [1,2,3,4,5,6,7,8,9,10,11,12]
print(f"data angka = {data_angka}")

def kurang_dari_5(data) :
    return data < 5
data_angka_new = list(filter(kurang_dari_5,data_angka))
print(f"data angka kurang dari 5 = {data_angka_new}")

   # menggunakan lambda
data_angka = [1,2,3,4,5,6,7,8,9,10,11,12]
data_angka_new2 = list(filter(lambda x : x < 8,data_angka))
print(f"data angka kurang dari 8 = {data_angka_new2}")

data_genap = list(filter(lambda x : x % 2==0, data_angka))
print(f"data angka genap = {data_genap}")

data_ganjil = list(filter(lambda x : x % 2==1, data_angka))
print(f"data angka ganjil = {data_ganjil}")

data_kelipatan3 = list(filter(lambda x : x % 3 == 0, data_angka))
print(f"data angka kelipatan 3 = {data_kelipatan3}\n")


## Anonymous function (curyying <-- Haskell Curry)
   # function biasa
def pangkat(angka, n) :
    hasil = angka**n
    return hasil
data_pangkat = pangkat(3,5)
print(f"menggunakan function biasa = {data_pangkat}")

   # menggunakan curying
def pangkat_2(n) :
    return lambda angka : angka**n
pangkat2 = pangkat_2(2)
print(f"pangkat2 = {pangkat2(5)}")
pangkat4 = pangkat_2(4)
print(f"pangkat24 = {pangkat4(5)}")
print(f"pangkat bebas = {pangkat_2(2)(3)}")




