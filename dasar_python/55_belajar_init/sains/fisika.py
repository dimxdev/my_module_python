## modul fisika

def jarak(kecepatan, waktu):
    return kecepatan*waktu

def waktu(jarak, kecepatan):
    return jarak/kecepatan

def kecepatan(jarak, waktu):
    return jarak/waktu

def input_user():
    jarak = int(input("masukkan jarak = "))
    kecepatan = int(input("masukkan kecepatan = "))
    waktu = int(input("masukkan waktu = "))
    return jarak, kecepatan, waktu



