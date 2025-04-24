import time
import os


# Fungsi untuk membersihkan layar terminal (untuk animasi lebih mulus)
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


# Fungsi untuk menggambar animasi orang dengan gerakan tangan berjoget
def animate_person():
    try:
        while True:
            # Posisi tangan atas (berjoget)
            clear_screen()
            print("   O  ")  # Kepala
            print("  /|\\ ")  # Badan dengan tangan kiri dan kanan berayun ke atas
            print("   |  ")  # Badan tetap
            print("  / \\ ")  # Kaki
            time.sleep(0.3)  # Delay antar frame

            # Posisi tangan bawah (berjoget)
            clear_screen()
            print("   O  ")  # Kepala
            print("  /|  ")  # Badan dengan satu tangan di bawah
            print("   |  ")  # Badan tetap
            print("  / \\ ")  # Kaki
            time.sleep(0.3)

            # Posisi tangan ke kiri (berayun)
            clear_screen()
            print("   O  ")  # Kepala
            print("  -|\\ ")  # Badan dengan tangan kiri berayun
            print("   |  ")  # Badan tetap
            print("  / \\ ")  # Kaki
            time.sleep(0.3)

            # Posisi tangan ke kanan
            clear_screen()
            print("   O  ")  # Kepala
            print(" \\|  ")  # Badan dengan tangan kanan berayun
            print("   |  ")  # Badan tetap
            print("  / \\ ")  # Kaki
            time.sleep(0.3)

    except KeyboardInterrupt:
        clear_screen()
        print("Animasi Berhenti")


# Jalankan animasi
animate_person()
