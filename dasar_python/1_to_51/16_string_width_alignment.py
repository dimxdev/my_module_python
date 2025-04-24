judul = "STRING WIDTH & AlIGNMENT"
print(judul.center(30, "-"))

data_nama = "Dimas"
data_usia = 18
data_alamat = "jepara"
data_tinggi = 200

## string standard
data_gabungan = f"nama = {data_nama}, usia = {data_usia}, alamat = {data_alamat}, tinggi = {data_tinggi} \n"
print(data_gabungan)

## string multiline menggunkan enter \n
data_gabungan = f"nama = {data_nama}, \nusia = {data_usia}, \nalamat = {data_alamat}, \ntinggi = {data_tinggi}"
print(data_gabungan)

## string multiline menggunakan kutip tripels
data_gabungan = f"""
nama   = {data_nama}
usia   = {data_usia}
alamat = {data_alamat}
tinggi = {data_tinggi}
""" # bisa diatur semau kita
print(data_gabungan)

##  mengatur lebar
data_gabungan = f"""
nama   = {data_nama:>8}
usia   = {data_usia:>8}
alamat = {data_alamat:>8}
tinggi = {data_tinggi:>8}
""" 
print(data_gabungan)

"""
   :> untuk rata kanan
   :< untuk rata kiri
   :^ untuk rata tengah
"""
