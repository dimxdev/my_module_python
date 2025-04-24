# latihan komparasi 
# membuat gabungan area rentang angka

# n < 3 atau n < 10
print("==== n < 3 atau n < 10 ====")
n = int(input("masukkan angka kurang dari 3 atau lebih dari 10 = "))
print("nilai n =", n)
kurangDari = n < 3
lebihDari = n > 10
print("kurang dari 3 =", kurangDari)
print("lebih dari 10 =", lebihDari)
iscorrect = kurangDari | lebihDari
print(iscorrect)
hasil = (n < 3) | (n > 10)
print("n < 3 atau n > 10 =", hasil)

print("\n")

# 3 < n < 10  
print("==== 3 < n < 10 ====")
n = int(input("masukkan angka lebih dari 3 dan kurang dari 10 = "))
print("nilai n =", n)
kurangDari = n < 10
lebihDari = n > 3
print("kurang dari 10 =", kurangDari)
print("lebih dari 3 =", lebihDari)
iscorrect = kurangDari & lebihDari
print(iscorrect)
hasil = 3 < n < 10
print("3 < n < 10 =" , hasil)
