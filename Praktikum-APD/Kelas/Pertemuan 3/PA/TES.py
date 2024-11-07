import os
import re
import time
def clear():
    os.system('cls||clear')

while True:
    clear()
    print("=" * 45)
    print("\t\tPROGRAM CRUD")
    print("=" * 45)
    print("[1]. Lihat Produk\n[2]. Tambah Produk\n[3]. Edit Produk\n[4]. Hapus Produk\n[5]. Lihat Profit\n[0]. Keluar")
    print("=" * 45)
    pilihanMenu = input("Masukkan nomor menu : ")
    try:
            pola = r"[^\w\s]"
            karakter_spesial = re.findall(pola, pilihanMenu)
            if karakter_spesial:
                print("Karakter spesial terdeteksi:")
                print(karakter_spesial)
                input("Tekan enter untuk melanjutkan. . . . .")
            else:
                print("Tidak ada karakter spesial yang ditemukan.")
            if pilihanMenu.isalpha():
                raise ValueError("Masukkan menu menggunakan angka!")
            if any(char.strip() for char in pilihanMenu.strip()):
                raise ValueError("Masukkan pilihan menu!")
    except ValueError as e:
            print(e)
            input("Tekan enter untuk melanjutkan. . . . .")
    if pilihanMenu == "1":
        clear()
        print("Anda berhasil masuk ke menu 1")
        input("Tekan enter untuk melanjutkan. . . . .")
    elif pilihanMenu == "2":
        clear()
        print("Anda berhasil masuk ke menu 2")
        input("Tekan enter untuk melanjutkan. . . . .")
    elif pilihanMenu == "3":
        clear()
        print("Anda berhasil masuk ke menu 3")
        input("Tekan enter untuk melanjutkan. . . . .")
    elif pilihanMenu == "4":
        clear()
        print("Anda berhasil masuk ke menu 4")
        input("Tekan enter untuk melanjutkan. . . . .")
    elif pilihanMenu == "5":
        clear()
        print("Anda berhasil masuk ke menu 5")
        input("Tekan enter untuk melanjutkan. . . . .")
    elif pilihanMenu == "0":
        clear()
        print("Anda berhasil masuk ke menu 0")
        input("Tekan enter untuk melanjutkan. . . . .")
        break