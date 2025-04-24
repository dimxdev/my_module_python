from numbers import Number

def tambah(a,b):
    if not isinstance(a,Number) or  not isinstance(b,Number):
        raise "input harus angka"
    return a + b
print(tambah(4,7))

# 1
angka = 0
try :
    hasil = 10/angka
except Exception as error_massage :
    print(error_massage)

# 2
angka2 = 0
try :
    hasil = 10/angka2
except ZeroDivisionError as error_msg :
    print(error_msg)
