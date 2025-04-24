print("=====OPERASI DAN MANIPULASI STRING 1=====")

# 1. menyambung string
namaPertama = "Dimas"
namaTengah = "Brotowali"
namaAkhir = "Hidayatullah"

namaLengkap = namaPertama + " " + namaTengah + " " + namaAkhir # klo ditambahkan di variabel pake + bukan koma
print(namaLengkap)
print(namaPertama, namaTengah, namaAkhir) # klo ditambahkan di print bisa pake koma bisa pake +


# 2. menghitung panjang string
panjang = len(namaLengkap)
print("panjang dari (" + namaLengkap + ") = " + str(panjang))

# 3. operator untuk string 
  # mengecek apakah ada komponen char atau string di dalam string
b = "b"
check = b in namaLengkap
print("apakah 'b' ada didalam " + namaLengkap + "? " + str(check))

B = "B"
check = B in namaLengkap
print("apakah 'B' ada didalam " + namaLengkap + "? " + str(check))

b = "b"
check = b not in namaLengkap
print("apakah 'b' tidak ada didalam " + namaLengkap + "? " + str(check))

  # mengulang string
print("wk"*5)
print(5*"wk")

  # indexing
print("print index ke-0 : " + namaLengkap[0])
print("print index ke-5 : " + namaLengkap[5])
print("print index ke-(-1) : " + namaLengkap[-1])
print("print index ke-(0-3) : " + namaLengkap[0:4]) # tanda (:) dibaca sampai klo di python misal pengen sampai index ke tiga maka harus dilebihkan 1 pada syntaknya(bawaan python)
print("print index ke-(7-3) : " + namaLengkap[10:20]) # tanda (:) dibaca sampai klo di python misal pengen sampai index ke tiga maka harus dilebihkan 1 pada syntaknya(bawaan python)
print("print index ke-(0, 2, 4, 6, 8, 10, 12) : " + namaLengkap[0:13:2]) # tanda (:) kedua itu dianggap pembagi
 
  # item paling kecil 
print("item paling kecil dari " + namaLengkap + " = " + min(namaLengkap)) # abjad huruf
  
  # item paling besar
print("item paling kecil dari " + namaLengkap + " = " + max(namaLengkap))

ascii_code = ord(" ")
print("ascii code dari spasi : " + str(ascii_code))
data = 109
print("char untuk ascii " + str(data) + " : " + chr(data))

# 4. operator dalam bentuk method(prosedur & function)
data = "dimis britiwili hidiyiti"
jumlah = data.count("i")
print("jumlah huruf i pada (" + data + ") : " + str(jumlah))




