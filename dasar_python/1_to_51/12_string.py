print("=====STRING=====")
data = "ini adalah string"
print(data, type(data), "\n")

# cara membuat string
'''
    1. menggunakan single quote '...'
    2. menggunakan double quote "..."
'''
data = 'ini menggunakan single quote'
print(data)
data = "ini menggunakan double quote"
print(data, "\n")

# menggunakan 2 2 nya
print('"hello bro!"')
print('dimas :"ini adalah hari jum\'at"') # jadi tanda \ itu memberi tahu kepada python bahwa ini bukanlah syntak
print("dimas :\"ini adalah hari jum'at\"") 
data = "dimas :\"ini adalah hari jum'at\" \n"
print(data)

# menggunakan \
print("C:\\user\\ucup \n")

# tab
print("ucup\t\totong, saling berjauhan\n")

# newline
print("baris pertama.\nbaris kedua.") # LF -> line feed
print("baris pertama.\rbaris kedua.") # CR -> carriage return
print("baris pertama.\n\rbaris kedua.\n") # CRLF -> carriage return line feed

# string literal atau raw
  # hati-hati
print("c:\new folder")

  # menggunakan raw string
print(r'c:\new folder') # semua yg didalam raw dianggap string

  # multiple literal string
print("""
NAMA : DIMAS 
KELAS : C
""")

  # multiple literal string dan raw string
print(r"""
NAMA : DIMAS
KELAS : C \new class
website : www.dimas\new
""")

