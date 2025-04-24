# hanya membandingkan boolean 
# not, and, or, xor

print("\n====OPERASI LOGIKA====")

print("====NOT====")
a = True
b = not a
print("nilai boolean a =", a)
print("nilai boolean b =", b)

print("====AND====")
a = True
b = True
c = a & b
print(a, " and", b, "=", c )
a = True
b = False
c = a & b
print(a, " and", b, "=", c )
a = False
b = True
c = a & b
print(a, "and", b, "=", c )
a = False
b = False
c = a & b
print(a, "and", b, "=", c )

print("====OR====")
a = True
b = True
c = a | b
print(a, " or", b, "=", c )
a = True
b = False
c = a | b
print(a, " or", b, "=", c )
a = False
b = True
c = a | b
print(a, "or", b, "=", c )
a = False
b = False
c = a | b
print(a, "or", b, "=", c )

print("====XOR====")
a = True
b = True
c = a ^ b
print(a, " XOR", b, "=", c )
a = True
b = False
c = a ^ b
print(a, " XOR", b, "=", c )
a = False
b = True
c = a ^ b
print(a, "XOR", b, "=", c )
a = False
b = False
c = a ^ b
print(a, "XOR", b, "=", c )



