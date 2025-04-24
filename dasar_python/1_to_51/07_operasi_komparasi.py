#setiap hasil operasi komparasi pasti bernilai boolean
# >, <, >=, <=, ==, !=, is, is not

print("\n==== OPERASI KOMPARASI ====")

a = 4
b = 2

print("== lebih besar dari (>) ==")
hasil = a > 3
print(a, ">", 3, "=", hasil)
hasil = b > 3
print(b, ">", 3, "=", hasil)

print("== lebih kecil dari (<) ==")
hasil = a < 3
print(a, "<", 3, "=", hasil)
hasil = b < 3
print(b, "<", 3, "=", hasil)  
hasil = a > b
print(a, ">", b, "=", hasil)  

print("== lebih kecil dari samadengan (<=) ==")
hasil = a <= 3
print(a, "<=", 3, "=", hasil)
hasil = b <= 2
print(b, "<=", 3, "=", hasil)  

print("== lebih besar dari samdengan (>=) ==")
hasil = a >= 4
print(a, ">=", 3, "=", hasil)
hasil = b >= 3 
print(b, ">=", 3, "=", hasil)

print("== samadengan (==) ==")
hasil = a == 4
print(a, "==", 3, "=", hasil)
hasil = b == 3 
print(b, "==", 3, "=", hasil)

print("== tidak samadengan (!=) ==")
hasil = a != 4
print(a, "!=", 3, "=", hasil)
hasil = b != 3 
print(b, "!=", 3, "=", hasil)

print("== object identitiy (is) ==")
x = 5
y = 5
print("nilai x =", x, ", id=", hex(id(x)))
print("nilai y =", y, ", id=", hex(id(y)))
hasil = x is y
print("x is y =", hasil)
x = 5
y = 6
print("nilai x =", x, ", id=", hex(id(x)))
print("nilai y =", y, ", id=", hex(id(y)))
hasil = x is y
print("x is y =", hasil)

print("== object identitiy (is not) ==")
x = 5
y = 5
print("nilai x =", x, ", id=", hex(id(x)))
print("nilai y =", y, ", id=", hex(id(y)))
hasil = x is not y
print("x is y =", hasil)
x = 5
y = 6
print("nilai x =", x, ", id=", hex(id(x)))
print("nilai y =", y, ", id=", hex(id(y)))
hasil = x is not y
print("x is y =", hasil, "\n")





