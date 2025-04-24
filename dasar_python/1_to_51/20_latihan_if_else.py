judul = "LATIHAN MEMBUAT KALKULATOR SEDERHANA MENGGUNAKAN IF ELSE"
print("\n", judul.center(70, "-"), "\n")

angka_pertama = float(input("masukkan angka pertama : "))
operator = input("masukkan operator (+, -, x, :) : ")
angka_kedua = float(input("masukkan angka kedua : "))

if operator == "+" :
    hasil = angka_pertama + angka_kedua
    print(f"hasil {angka_pertama} + {angka_kedua} = {hasil}")
elif operator == "-" :
    hasil = angka_pertama - angka_kedua
    print(f"hasil {angka_pertama} - {angka_kedua} = {hasil}")
elif operator == "*" or operator == "x" :
    hasil = angka_pertama * angka_kedua
    print(f"hasil {angka_pertama} x {angka_kedua} = {hasil}")
elif operator == "/" or operator == ":" :
    hasil = angka_pertama / angka_kedua
    print(f"hasil {angka_pertama} : {angka_kedua} = {hasil}")
else :
    print("operator yang anda masukkan tidak ada di daftar kalkulator kami")
