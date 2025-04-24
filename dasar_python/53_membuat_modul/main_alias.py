import os 
os.system("cls")

from matematika import tambah as tbh
from matematika import kali as kl
from matematika import pangkat as pkt

import matematika as mtk 

tambah = mtk.tambah(1,2,3,4,5,6,7,8,9)
print(f"hasil tambah\t= {tambah}")

kali = kl(1,2,3,4)
print(f"hasil kali\t= {kali}")

pangkat = pkt(3)
print(f"hasil pangkat\t= {pangkat(6)}")
print("-"*25)