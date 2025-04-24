judul = " LIST/ ARRAY "
print(judul.center(30, "="))

## list data angka
list_angka = [1, 2, 3, 4, 5, 5]
print(list_angka)

## list data string
list_string = ["otong", "ucup", "dimas", "tuntin"]
print(list_string)

## list data boolean
list_boolean = [True, False, True, True]
print(list_boolean)

## list data campuran
list_campuran = [True, "ucup", 3, "makan"]
print(list_campuran)

## cara alternatif membuat list
list_range = range(2, 10, 3) # start, stop, step
print(list(list_range))

## membuat list menggunakan for loop (list Comprehension)
list_for = [i for i in range(0,10)]
print(list_for)

list_for = [i*2 for i in range(0,10)]
print(list_for)

list_for = [i**2 for i in range(0,10)]
print(list_for)


## membuat list menggunakan for & if
list_forIf = [i for i in range(0,10) if i != 5]  
print(list_forIf)

list_forIf = [i for i in range(0,10) if i == 5]  
print(list_forIf)

list_forIf = [i for i in range(0,10) if i % 2 == 0]  
print(list_forIf)

list_forIf = [i for i in range(0,10) if i % 2 == 1]  
print(list_forIf)


## membuat list menggunakan while loop
data_list = []
i = 0
while i < 10 :
    data_list.append(i)
    i += 1
print(data_list)

# 2 logika beda tapi output sama
data_list = []
i = 0
while i < 10 :
    data_list.append(i)
    if i % 2 == 0 :
        i += 2    
print(data_list)
data_list = []
i = 0
while i < 10 :
    if i % 2 == 0 :
        data_list.append(i)
    i += 1    
print(data_list)


# 2 logika beda tapi output sama
data_list = []
i = 0
while i < 10 :
    data_list.append(i)
    if i % 2 == 1 :
        i += 1    
    i += 1
print(data_list)
data_list = []
i = 0
while i < 10 :
    if i % 2 == 1 :
        data_list.append(i)
    i += 1    
print(data_list)
print("program selesai \n")