import os
os.system("cls")

print(f"{" **KWARGS ":^20}") ## akan menghasilkan output dictionary
print("-"*20)


def data_diri(nama, tinggi, berat) :
    print(f"nama\t= {nama}\ntinggi\t= {tinggi}cm\nberat\t= {berat}kg\n")
data_diri("ucup", 12, 34)

def data_diri2(**kwargs) :
    nama = kwargs["nama"]
    tinggi = kwargs["tinggi"]
    berat = kwargs["berat"]
    print(f"{nama} punya tinggi {tinggi}cm dan berat {berat}kg\n")
data_diri2(nama="ucup", tinggi=23, berat=10)

def math(*data, **kwargs) :
    if kwargs["opsii"] == "tambah" :
        output = 0
        for angka in data :
            output += angka
    elif kwargs["opsii"] == "kali" :
        output = 1
        for angka in data :
            output *= angka
    else :
        print("opsi tidak ditemukan")

    return output
tambah = math(1,2,3,4, opsii = "tambah")
print(f"hasil tambah = {tambah}")

kali = math(1,2,3,4, opsii = "kali")
print(f"hasil kali = {kali}")
