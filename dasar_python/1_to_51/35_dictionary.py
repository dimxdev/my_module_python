judul = " DICTIONARY "
print(judul.center(30, "="))


## menggunakan index
print("\n=== DATA LIST ===")
data_list = [1,2,4,5,6,9,7]
print(data_list[4], "\n")


## dictionary (dict) --> associative array
   # indentifier --> key
print("=== DATA DICTIONARY ===")
data_dict = {
    'key' : 'value',
    'uc' : 'ucup',
    'di' : 'dimas',
    "tu" : 'tuntin',
    'no' : 1000,
    'list' : data_list
}
print(data_dict['tu'])
print(data_dict['uc'])
print(data_dict['key'])
print(data_dict['no'])
print(data_dict['list'])

data_dict2 = {
    'key' : 'value',
    'di' : data_dict,
}
print(data_dict2['di'])
print("program selesai \n")