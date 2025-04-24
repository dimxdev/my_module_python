"""
   1. __main__ adalah top level code environtment
   2. syntak di python (__name__  = __main__)  --> akan terjadi jika berada pada file program utama 
"""

## __name dalam program utama 
print(f"nilai __name__ pada main.py = '{__name__}'")


import pungsi  # ---> tidak akan berjalan fungsi syntak __name__


## contoh menggunaan __name__
def tambah(ang1:int, ang2:int) -> int:
    return ang1 + ang2

if __name__ == "__main__":
    angka1 = 5
    angka2 = 10
    hasil = tambah(angka1, angka2)
    print(f"hasil tambah = {hasil}")
