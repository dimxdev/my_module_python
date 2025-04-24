import os 
os.system("cls")

print(f"{"NUM PY":^20}")
print("_"*20, "\n")

import numpy as num


## list
list_1 = [1,2,3,4]  # normal
list_2 = num.array([1,2,3,4])  # menggunakan numpy

print(f"list 1 = {list_1}")
# print(list_1**2) <-- akan error
print(f"list 2 = {list_2}")
halo = print(f"list 2 kuadrat = {list_2**list_2}")
print(f"list 2 pangkat 2 = {list_2**2}")
print("-"*35, "\n")


## matrix
matrix_1 = num.array([(1,2),(4,5)])
print(f"matrix 1 = \n{matrix_1}") 
print(f"matrix 1^2 = \n{matrix_1**2}") 

matrix_zero = num.zeros((3,2))
print(f"matrix zero = \n{matrix_zero}") 

matrix_one = num.ones((2,2))
print(f"matrix one = \n{matrix_one}") 

jumlah = matrix_1 + matrix_1*3 - matrix_one
print(f"jumlah = \n{jumlah}") 
print("-"*35, "\n")





