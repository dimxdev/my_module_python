import os
os.system("cls")

print(f"{"KONSTRUKTOR __INIT__":^25}")
print("_"*25, "\n")

class kucing:

    def __init__(self,nama,berat,warna,pemilik,statusJinak):
        self.nama = nama
        self.berat = berat
        self.warna = warna
        self.pemilik = pemilik
        self.jinak = statusJinak

    def cetak(self):
        print(f"namaku {self.nama}, aku adalah seekor kucing, buluku berwarna {self.warna}, berat badanku {self.berat}kg, nama majikanku adalah {self.pemilik}")


# kucing 1
amel = kucing("Amel", 30, "merah", "dimas", True)
print(amel.nama)
print(amel.nama, amel.warna, amel.pemilik, amel.jinak)
print(amel.__dict__)
amel.cetak()
print("-"*110, "\n")

# kucing2
wildan = kucing("wildan", 25, "putih", "dimas", False)
print(wildan.nama)
print(wildan.__dict__)
wildan.cetak()
print("-"*110, "\n")

