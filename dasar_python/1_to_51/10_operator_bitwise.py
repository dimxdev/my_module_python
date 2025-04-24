# operasi biner

a = 7 
b = 5

# bitwise OR (|)
c = a | b
print("\n=====OR=====")
print("nilai:", a, "binary:", format(a,"08b"))
print("nilai:", b, "binary:", format(b,"08b"))
print("------------------------------(|)")
print("nilai:", c, "binary:", format(c,"08b"))

# bitwise AND (&)
c = a & b
print("\n=====AND=====")
print("nilai:", a, "binary:", format(a,"08b"))
print("nilai:", b, "binary:", format(b,"08b"))
print("------------------------------(&)")
print("nilai:", c, "binary:", format(c,"08b"))

# bitwise XOR (^)
c = a ^ b
print("\n=====XOR=====")
print("nilai: ", a, "binary:", format(a,"08b"))
print("nilai: ", b, "binary:", format(b,"08b"))
print("------------------------------(^)")
print("nilai:", c, "binary:", format(c,"08b"))

# bitwise NOT (~)
c = ~a
print("\n=====NOT=====")
print("nilai: ", a, "binary:", format(a,"08b"))
print("------------------------------(~)")
print("nilai:", c, "binary:", format(c,"08b"))
print(25*"=", "\n")
d = 0b000000011
e = 0b111111111
hasilBalik = d ^ e
print("nilai: ", d, "binary:", format(d,"08b"))
print("nilai: ", e, "binary:", format(e,"08b"))
print("------------------------------(^)")
print("nilai:", hasilBalik, "binary:", format(hasilBalik,"08b"))

# sift right(>>)
c = a >> 2
print("\n=====(>>)=====")
print("nilai: ", a, "binary:", format(a,"08b"))
print("------------------------------(>>)")
print("nilai:", c, "binary:", format(c,"08b"))

# sift left(<<)
c = a << 2
print("\n=====(<<)=====")
print("nilai: ", a, "binary:", format(a,"08b"))
print("------------------------------(<<)")
print("nilai:", c, "binary:", format(c,"08b"))
