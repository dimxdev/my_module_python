judul = "IF ELSE"
print(judul.center(30, "-"))


"""
   <  : Lebih kecil
   >  : Lebih besar
   <= : Lebih kecil atau sama dengan
   >= : Lebih besar atau sama dengan
   == : Sama dengan
   != : Tidak sama dengan
   in : untuk memeriksa apakah suatu nilai ada dalam koleksi (seperti list, set, atau string).
   not: untuk membandingkan kesamaan secara terbalik.
   is : untuk mengecek apakah dua objek benar-benar sama (identik) di memori, bukan hanya nilainya.
"""

## 1. program if inline
nama = input("masukkan nama anda : ").lower()
if nama == "dimas" : print(f"kamu ckep abies {nama}")

## 2. program if indentation
if nama == "dimas" :
    print(f"kamu ckep abies {nama}")
    print(f"kamu ckep bgt {nama}")

## 3. program if else    
if nama == "dimas" :
    print(f"kamu ckep abies {nama}")
else :
    print(f"kamu jelek {nama}")

