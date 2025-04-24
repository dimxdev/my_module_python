import tkinter as tk


# Inisialisasi jendela Tkinter
window = tk.Tk()
window.geometry("500x400")
window.title("Orang Joget GUI")

# Membuat label untuk menampilkan animasi
label = tk.Label(window, font=("Courier", 20), bg="lightblue")
label.pack(fill="both", expand=True)

# Variabel untuk gerakan tangan
posisi_tangan = 0  # 0 untuk tangan di atas, 1 untuk tangan di bawah, 2 untuk kiri, 3 untuk kanan

# Fungsi untuk menggambar orang berjoget
def animate_person():
    global posisi_tangan
    
    # Tentukan gambar animasi berdasarkan posisi tangan
    if posisi_tangan == 0:
        # Tangan ke atas
        text = "   O  \n  /|\\ \n   |  \n  / \\ "
    elif posisi_tangan == 1:
        # Tangan ke bawah
        text = "   O  \n  /|  \n   |  \n  / \\ "
    elif posisi_tangan == 2:
        # Tangan kiri
        text = "   O  \n  -|\\ \n   |  \n  / \\ "
    elif posisi_tangan == 3:
        # Tangan kanan
        text = "   O  \n \\|  \n   |  \n  / \\ "

    # Update label dengan teks animasi
    label.config(text=text)

    # Tentukan posisi tangan berikutnya
    posisi_tangan = (posisi_tangan + 1) % 4  # Berulang dari 0 hingga 3

    # Jadwalkan animasi berikutnya dalam 300 ms
    window.after(300, animate_person)

# Mulai animasi
animate_person()

# Jalankan aplikasi GUI
window.mainloop()
