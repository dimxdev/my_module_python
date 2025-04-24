judul = "METHOD DALAM STRING"
print(judul.center(30,"-"))

"""
   ada 3 cara dalam penulisan method :
     1. ditulis dalam variabel utama
     2. ditulis di dalam variabel lain
     3. ditulis di dalam print
"""

## Merubah case pada string
  # merubah semua ke upper case 
text = "hello python".upper() # cara 1
print("uppercase: " + text) 

text = "Python is Awesome!"
upper_text = text.upper() # cara 2
print("Uppercase:", upper_text) 

print("Uppercase:", text.upper(), "\n") # cara 3 


  # merubah semua ke lower case
text = "HELLO PYTHON".lower() # cara 1
print("lowercase: " + text) 

text = "Python is Awesome!"
lower_text = text.lower() # cara 2
print("lowercase:", lower_text) 

print("lowercase:", text.lower(), "\n") # cara 3 


## pengecekan kondisi menggunakan isX method
  # pengecekkan lower case
salam = "hallo"
apakah_lowerCase = salam.islower()
print("apakah", salam, "is lowercase:", apakah_lowerCase, "")

  # pengecekkan upper case
salam = "hallo"
apakah_upperCase = salam.isupper()
print("apakah", salam, "is upperCase:", apakah_upperCase, "\n")


## mengecek komponen startswith() dan endswith()
halo = "dimas bro"
cekStart = halo.startswith("dimas")
print("apakah '" + halo + "' start with 'dimas'?", cekStart)

halo = "dimas bro"
cekEnd = halo.endswith("bro")
print("apakah '" + halo + "' end with 'bro'?", cekEnd , "\n")


## penggabungan komponen j0in() split()
pisah = ["aku", "sayang", "kamu"]
gabung = ",".join(pisah)
print(gabung)

gabung = " ".join(pisah)
print(gabung)

gabung = " ehm ".join(pisah)
print(gabung)

gabung = "akuehmsayangehmkamu"
pisah = gabung.split("ehm")
print(pisah, "\n")


## alokasi karakter rjust(), ljust(), center()
kanan = "kanan"
kanankan = kanan.rjust(15)
print("'" + kanankan + "'")
kanankan = kanan.center(15, "=")
print("'" + kanankan + "'", "\n")

kiri = "kiri"
kirikan = kiri.ljust(15)
print("'" + kirikan + "'")
kirikan = kiri.center(15, "=")
print("'" + kirikan + "'", "\n")

tengah = "tengah"
tengahkan = tengah.center(15)
print("'" + tengahkan + "'")
tengahkan = tengah.center(15, "=")
print("'" + tengahkan + "'")
