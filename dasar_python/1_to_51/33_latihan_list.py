judul = " PROGRAM LIST BUKU "
print(judul.center(30, "="))

list_buku = []
while True:
    print("\nmasukkan judul buku")
    judul = input("judul buku = ")
    penulis = input("penulis buku = ")

    buku_baru = [judul, penulis]
    list_buku.append(buku_baru)
    # print(list_buku)

    print("\nDATA BUKU")
    for index, buku in enumerate(list_buku):
        print(f"{index + 1}  |  {buku[0]}  |  {buku[1]}")

    isLanjut = input("apakah dilanjutkan (y/n) : ")   
    if isLanjut == "y":
        continue  # Kembali ke awal loop
    elif isLanjut == "n":
        break  # Keluar dari loop
    else:
        print("Maaf, karakter yang Anda masukkan tidak sesuai syarat. Masukkan 'y' untuk lanjut atau 'n' untuk berhenti.")

print("program selesai\n")

        



