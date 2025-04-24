def judul() :
   import os
   os.system("cls")
   print("="*30)
   print(f"{" HITUNG LUAS DAN ":^30}")
   print(f"{" KELILING PERSEGI PANJANG ":^30}")
   print("="*30)

def input_user() :
   input1 = int(input("masukkan panjang : "))
   input2 = int(input("masukkan lebar : "))
   return input1, input2

def luas(panjang, lebar) :
   return panjang*lebar

def keliling(panjang, lebar) :
   return 2*panjang + 2*lebar

def cetak(messege, hasil) :
   print(f"hasil perhitungan {messege} = {hasil}")


while True :
   judul()
#    mengetahui = input_user()
#    panjang = mengetahui[0]
#    lebar = mengetahui[1]

   panjang, lebar = input_user()
   hasilluas = luas(panjang, lebar)
   hasilkeliling = keliling(panjang, lebar)
   cetak("luas", hasilluas)
   cetak("keliling", hasilkeliling)

   iscontiue = input("apakah anda ingin lanjut (y/n) : ")
   if iscontiue == "n" :
      break
   else :
      continue
print("program selesai\n")

# while True :
#    judul()
# #    mengetahui = input_user()
# #    panjang = mengetahui[0]
# #    lebar = mengetahui[1]
#    a = int(input("masukkan angka (1 untuk menghitung luas ; 2 untuk menhitung keliling): "))
#    if a == 1 :
#       panjang, lebar = input_user()
#       luas = luas(panjang, lebar)
#       cetak("luas", luas)
#    else :
#       panjang, lebar = input_user()
#       keliling = keliling(panjang, lebar)
#       cetak("keliling", keliling)
            
#    iscontiue = input("apakah anda ingin lanjut (y/n) : ")
#    if iscontiue == "n" :
#       break
# print("program selesai\n")