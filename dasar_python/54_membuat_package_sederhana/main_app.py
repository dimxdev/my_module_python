import os
os.system("cls")

print("_"*30, "\n")
print(f"{"PACKAGE SEDERHANA":^30}")
print("_"*30, "\n")

import sains.matematika as mtk
from sains import fisika as fsk
from sains.fisika import jarak as jrk

hasil_tambah = mtk.tambah(3,4,5,6,7,8,9,90)
print(f"hasil tambah = {hasil_tambah}")

hasil_kali = mtk.kali(3,4,5,6,7,8,9,90)
print(f"hasil kali = {hasil_kali}")

hasil_pangkat = mtk.pangkat(3)
print(f"hasil pangkat = {hasil_pangkat(8)}")
print("-"*30, "\n")


jarak, kecepatan, waktu = fsk.input_user()
hasil_jarak = fsk.jarak(kecepatan, waktu)
print(f"jarak\t  = {hasil_jarak}")

hasil_kecepatan = fsk.kecepatan(jarak, waktu)
print(f"kecepatan = {hasil_kecepatan}")

hasil_waktu = fsk.waktu(jarak, kecepatan)
print(f"waktu\t  = {hasil_waktu}")
print("-"*30, "\n")





