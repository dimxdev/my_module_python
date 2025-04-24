judul = " CONTINUE & PASS "
print(judul.center(40, "="))

## pass (berfungsi untuk mengisi block kosong yg belom di isi untuk menghindari syntak error)
angka = 0
print(f"angka awal = {angka}")
while angka < 7 :
    angka += 1
    print(f"angka = {angka}")
    if angka == 3 :
        pass
print("kode selesai \n")

## continue (berfungsi untuk melewati perintah setelah kondisi)
angka = 0
print(f"angka awal = {angka}")
while angka < 7 :
    angka += 1
    if angka == 3 :
        # print("yey!")
        continue
    print(f"angka = {angka}")
print("kode selesai \n")

angka = 0
print(f"angka awal = {angka}")
while angka < 10 :
    angka += 1
    if angka % 2 == 1 :
        print("angka ganjil dihapus")
        continue
    print(f"angka = {angka}")
print("kode selesai \n")