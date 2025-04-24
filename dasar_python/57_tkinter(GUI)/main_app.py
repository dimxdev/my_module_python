import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo

## init
window = tk.Tk()
window.configure(bg="white")
window.geometry("700x400")
window.resizable(True,False)
window.title("GUI ACU")


## variable dan functon
NAMA_DEPAN = tk.StringVar()
NAMA_BELAKANG = tk.StringVar()

def tombol_click():
    pesan = f"Halo {NAMA_DEPAN.get()} {NAMA_BELAKANG.get()}, Ganteng"
    showinfo(title="hei", message=pesan)


## frame input
input_frame = ttk.Frame(window)
input_frame.pack(padx=10,pady=10,fill="x",expand=True) # penempatan Grid, pack, place


# 1. label nama depan
nama_depan_label = ttk.Label(input_frame, text="nama depan : ")
nama_depan_label.pack(padx=10, fill="x", expand=True)

# 2. entry nama depan
nama_depan_entry = ttk.Entry(input_frame, textvariable=NAMA_DEPAN)
nama_depan_entry.pack(padx=10, fill="x", expand=True)

# 3. label nama belakang
nama_belakang_label = ttk.Label(input_frame, text="nama belakang : ")
nama_belakang_label.pack(padx=10, fill="x", expand=True)

# 4. entry nama belakang
nama_belakang_entry = ttk.Entry(input_frame, textvariable=NAMA_BELAKANG)
nama_belakang_entry.pack(padx=10, fill="x", expand=True)

# 5. tombol
tombol_sapa = ttk.Button(input_frame, text="sapa", command=tombol_click)
tombol_sapa.pack(padx=10,pady=10,fill="x",expand=True)


## main loop window
window.mainloop()