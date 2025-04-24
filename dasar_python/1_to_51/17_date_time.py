import datetime as dt
import locale
import os

# Mengatur locale ke bahasa Indonesia
locale.setlocale(locale.LC_TIME, 'id_ID.UTF-8')

os.system("cls")
hari_ini = dt.date.today()
print(hari_ini)
print(f"hari ini adalah hari {hari_ini:%A}")

tanggal = dt.date(2006, 1, 15)
print(tanggal)
print(f"hari = {tanggal:%a}")

"""
   %A: Digunakan untuk mendapatkan nama hari dalam teks lengkap, seperti Monday, Tuesday, dll.
   %a: Nama hari dalam bentuk singkat. Contoh: Sun, Mon, Tue.
   %w: Menampilkan indeks hari dalam minggu, dengan 0 sebagai Minggu. Contoh: 0 untuk Minggu, 1 untuk Senin.
   %d: Hari dalam bulan sebagai angka dua digit. Contoh: 01, 24.
"""

now = dt.datetime.now()
print(now)

## project untuk mengetahui hari kelahiran 

# input_tanggal = input("masukkan tanggal lahir kamu (format yyyy-mm-dd) : ")
# tanggal = dt.datetime.strptime(input_tanggal, "%Y-%m-%d").date()
# print(f"tanggal lahirmu adalah {tanggal}")
# print(f"hari lahirmu adalah {tanggal:%A}") 

print("\nmasukkan tanggal lahir anda")
tanggal = int(input("tanggal  : "))
bulan = int(input("bulan    : "))
tahun = int(input("tahun    : "))
tanggal_lahir = dt.date(tahun, bulan, tanggal)
hari_ini = dt.date.today()
umur_sekarang_hari = hari_ini - tanggal_lahir
umur_sekarang_tahun = umur_sekarang_hari // 365  
umur_bulan_sisa = (umur_sekarang_hari.days % 365) // 30
print(f"tanggal lahir anda adalah : {tanggal_lahir}")
print(f"anda lahir di hari : {tanggal_lahir:%A}")
print(f"umur anda sekarang adalah : {umur_sekarang_hari.days} hari")
print(f"umur anda sekarang adalah : {umur_sekarang_tahun.days} tahun {umur_bulan_sisa} bulan \n")


