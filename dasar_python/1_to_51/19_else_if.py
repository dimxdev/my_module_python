judul = "ELSE IF / ELIF"
print(judul.center(30, "-"))

nama = input("masukkan nama petugas : ").lower()
if nama == "asep" :
    print(f"{nama} adalah petugas kantor ini")
elif nama == "dudung" :
    print(f"{nama} adalah petugas kantor ini")
elif nama == "dimas" :
    print(f"{nama} adalah petugas kantor ini")
else :
    print(f"{nama} bukanlah petugas")


nama = input("masukkan nama petugas : ").lower()
petugas = ["dimas", "asep", "dudung", "ali", ]
if nama in petugas :
    print(f"{nama} adalah petugas")
else :
    print(f"{nama} bukanlah petugas")