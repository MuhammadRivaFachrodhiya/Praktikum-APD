# CRUD "Manajemen Keuntungan dari Suatu Perusahaan ATK"
from login import *
from programcrud import *
import os
import time

# Bagian Menu Utama
def main():
    try:
        while True:
            clear()
            print("=== Sistem Manajemen Keuntungan Perusahaan ATK ===")
            print("1. Login")
            print("2. Registrasi")
            print("3. Keluar")
            pilihan = input("Pilih menu : ")

            if pilihan == "1":
                clear()
                statusLogin = login() 
                
                if statusLogin: 
                    role, username = statusLogin
                    if role == "Owner":
                        ownerMenu()
                    else:
                        adminMenu()
                else:
                    input("Tekan Enter untuk melanjutkan...")
            elif pilihan == "2":
                clear()
                registrasi()
                loading()
                print()
                clear()
                print("Registrasi berhasil! Silahkan kembali login!")
                lanjut()
            elif pilihan == "3":
                clear()
                print("Terima kasih telah menggunakan program ini! Program akan tertutup secara otomatis dalam 5 detik. . . .")
                loading(102,5)
                exit()
    except Exception as e:
            print(f"Terjadi kesalahan: {str(e)}")


main()