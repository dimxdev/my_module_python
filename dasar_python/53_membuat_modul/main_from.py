import os 
os.system("cls")

from matematika import tambah, kali, pangkat
# from matematika import * (untuk ambil semua)

tambah = tambah(1,2,3,4,5,6,7,8,9)
print(f"hasil tambah\t= {tambah}")

kali = kali(1,2,3,4)
print(f"hasil kali\t= {kali}")

pangkat = pangkat(3)
print(f"hasil pangkat\t= {pangkat(6)}")
print("-"*25)