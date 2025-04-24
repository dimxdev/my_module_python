print("\n===== OPERASI ARITMATIKA =====")

a = 7
b = 3

#penjumlahan
hasil = a + b
print(a, "+", b, "=", hasil)

#pengurangan
hasil = a - b
print(a, "-", b, "=", hasil)

#perkalian
hasil = a * b
print(a, "*", b, "=", hasil)

#pembagian
hasil = a / b
print(a, "/", b, "=", hasil)

#perpangkatan
hasil = a ** b
print(a, "**", b, "=", hasil)

#floor division
hasil = a // b
print(a, "//", b, "=", hasil)

#prioritas operasi
 # 1. ()
 # 2. perpangkatan 
 # 3. perkalian dkk 
 # 4. penjumlahan dan pengurangan
a = 3
b = 5
c = 7
hasil = (a + b) * c / b ** a - c // b
print("(", a, "+", b, ") *", c, "/", b, "**", a, "-", c, "//", b, "=", hasil)

