#tipe data standar
dataInteger = 11
print("data:", dataInteger, "  ",  "bertipe:", type(dataInteger))

dataFloat = 1,5
print("data:", dataFloat, "  ",  "bertipe:", type(dataFloat))

dataString = "halo dek"
print("data:", dataString, "  ", "bertipe:", type(dataString))

dataBool = True
print("data:", dataBool, "  " "bertipe:", type(dataBool))


#tipe data khusus
 # 1. bilangan kompleks
dataComplex = complex(5,6)
print("data:", dataComplex, "  ", "bertipe:", type(dataComplex))

 # 2. tipe data dari bahasa c
from ctypes import c_double, c_char

dataCDouble = c_double(10.5)
print("data:", dataCDouble, "  ", "bertipe:", type(dataCDouble))

