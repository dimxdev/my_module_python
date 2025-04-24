#mengkonversi temperatur satu ke temperatur lain

print("\n===== KONVERSI TEMPERATUR =====")

celcius = float(input("masukkan suhu celcius: "))
print("suhu celcius:", celcius, "celcius")

#celcius to fahrenheit (9/5 * celcius + 32)
fahrenheit = ((9/5) * celcius) + 32
print("suhu dalam fahrenheit:", fahrenheit, "fahrenheit")

#celcius to reamur (4/5 * celcius)
reamur = (4/5) * celcius
print("suhu dalam reamur:", reamur, "reamur")

#celcius to kelvin (celcius + 273)
kelvin = celcius + 273
print("suhu dalam kelvin:", kelvin, "kelvin")


print("\n===== MENGHITUNG LUAS DAN KELILING SEGITIGA ====")
print("== LUAS ==")
alas = int(input("masukkan alas segitiga: "))
tinggi = int(input("masukkan tinggi segitiga: "))
luasSegitiga = (1/2) * alas * tinggi
print("luas segitiga:", luasSegitiga)

print("==== KELILING ====")
sisi = int(input("masukkan sisi segitiga: "))
kelilingSegitiga = sisi * 3
print("keliling segitiga:", kelilingSegitiga)


print("\n===== MENGHITUNG LUAS DAN KELILING lingkaran ====")
jarijari = int(input("masukkan jari-jari lingkaran: "))
luasLingkaran = (22/7) * (jarijari ** 2)
kelilingLingkaran = (22/7) * jarijari * 2
print("Luas lingkaran:", luasLingkaran)
print("keliling lingkaran:", kelilingLingkaran, "\n")







