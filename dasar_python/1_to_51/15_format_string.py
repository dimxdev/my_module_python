judul = "FORMAT STRING"
print(judul.center(30,"-"))

## format string ini berguna supaya tidak perlu menambahkan tanda + atau , saat ingin mencetak sesuatu
## string
nama = "ucup"
format_string = f"nama = {nama}"
print(format_string)
print(f"nama = {nama}") 

## boolean 
boolean = True
format_string = f"boolean = {boolean}"
print(format_string)

## angka 
   # normal
angka = 200
format_string =f"angka = {angka}"
print(format_string)

"""
   :d memberitahu Python untuk memformat nilai sebagai bilangan bulat desimal non float (integer in decimal format).
   :f untuk angka dengan desimal (floating-point).
   :x untuk angka dalam format heksadesimal (hexadecimal).
   :b untuk angka dalam format biner (binary).
   :o digunakan untuk memformat angka sebagai bilangan bulat dalam sistem oktal
   :e untuk format notasi eksponensial.
   :, untuk menampilkan koma angka ordo ribuan
   :+ untuk menampilkan lambang plus atau minus
   :% untuk menampilkan persen
"""

   # bilangan bulat
angka = 20
format_string =f"angka = {angka:d}"
print(format_string)

  # bilangan dengan ordo ribuan 
angka = 200000098830
format_string = f"angka = {angka:,}"
print(format_string)

   # bilangan desimal
angka = 20.7080098830
format_string = f"angka = {angka:.2f}" # memberitahukan bahwa yg di cetak hanya 2 angka dibelakang koma
print(format_string)

   # menamppilkan leanding zero 
angka = 20.7080098830
format_string = f"angka = {angka:010.2f}" 
print(format_string)
format_string = f"angka = {angka:10.2f}" 
print(format_string)

   # menampilkan tanda + atau -
angka_minus = -20
angka_plus = 20.989876736764
format_string_minus = f"angka = {angka_minus:+}"
format_string_plus = f"angka = {angka_plus:+10.3f}"
print(format_string_minus)
print(format_string_plus)

   # format persen
angka = 0.50
format_string = f"angka = {angka:.1%}"
print(format_string)

   # melakukan operasi aritmatika didalam kurung kurawal
angka1 = 20
angka2 = 5
total = f"total a * b = {angka1*angka2}"
print(total)

   # format angka lain (binary, octal, hexadecimal)
angka = 290
format_binary1 = f"biner = {bin(angka)}"
format_binary2 = f"biner = {angka:b}"
print(format_binary1)
print(format_binary2)

format_octal1 = f"octal = {oct(angka)}"
format_octal2 = f"octal = {angka:o}"
print(format_octal1)
print(format_octal2)

format_hexadecimal1 = f"hexadecimal = {hex(angka)}"
format_hexadecimal2 = f"hexadecimal = {angka:x}"
print(format_hexadecimal1)
print(format_hexadecimal2)






 
