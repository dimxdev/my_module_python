print("===== INPUT USER =====\n")

#semua data yang kita input merupakan string
data = input("masukkan nama anda: ")
print("HELLO", data, "Selamat pagi", "  ",  type(data), "\n")

#jika ingin jadi integer/float lain maka harus di casting dulu
angka = int(input("masukkan angka berapapun: "))
print("angka yang anda masukkan adalah:", angka, "  ", type(angka), "\n")

#jika boolean maka harus di casting menjadi integer dulu
biner = bool(int(input("masukkan angka berapapun: ")))
print("angka yang anda masukkan adalah:", biner, "  ", type(biner), "\n")
