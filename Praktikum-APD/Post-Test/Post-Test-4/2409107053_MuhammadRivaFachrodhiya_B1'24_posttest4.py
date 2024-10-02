import os
import math
import time
# Mohon untuk mengisi kata "lanjut" dengan huruf kapital diawal kata
#Ngosongin Terminal
clear = lambda: os.system('cls')
#AutentikasiData
kesempatan_login = 3
username = "Ripa"
password = "053"

clear()
while kesempatan_login > 0:
    clear()
    log_user = input("Masukkan Username (Harap Input dengan Huruf!) : ")
    pass_user = input("Masukkan Password (Harap Input dengan Angka!) : ")
    clear()
    if log_user == username and pass_user == password:
        print("Anda Berhasil Login!")
        print("Anda Akan Masuk ke Program...")
        kesempatan_login = 0
        time.sleep(3)
        pass
    else:
        kesempatan_login -= 1
        print("Username atau Password yang Anda Input Salah! Mohon Coba Lagi!")
        print(f"Kesempatan anda tersisa {kesempatan_login}x")
        time.sleep(3)
        print("Terimakasih Telah Menggunakan Program Ini")
        if kesempatan_login == 0:
            exit()

while True:
    clear()
    print("=" * 65)
    print("\t Selamat Datang Di Kalkulator Bangun Datar")
    print("=" * 65)
    print(" 1. Persegi\n 2. Persegi Panjang\n 3. Segitiga\n 4. Lingkaran\n 5. Keluar")
    
    pilihan_program = input("Mau Pilih Program Apa? : ")

    if pilihan_program == "1":
        clear()
        print("Anda Memilih Persegi!")
        print(" 1. Luas?\n 2. Keliling?")
        pilihan_menu = input("Mau Menu Apa? : ")
        if pilihan_menu == "1":
            clear()
            print("Anda Memilih Luas")
            sisi = float(input("Masukkan Sisi Persegi yang Mau Anda Hitung! : "))
            clear()
            luas_persegi = sisi * sisi
            print(f"Luas Persegi Anda adalah {luas_persegi} cm\u00B2")
            keberlangsungan = input("\nMau Lanjut Apa Tidak? : ")
            clear()
            if keberlangsungan == "Lanjut":
                print("Program Akan Berjalan Kembali Dalam Waktu 5 detik")
                time.sleep(5)
            else:
                print("Terimakasih Telah Menggunakan Program Ini!")
                exit()
        elif pilihan_menu == "2":
            clear()
            print("Anda Memilih Keliling")
            sisi = float(input("Masukkan Sisi Persegi yang Mau Anda Hitung! : "))
            clear()
            keliling_persegi = sisi * 4
            print(f"Keliling Persegi Anda adalah {keliling_persegi} cm\u00B2")
            keberlangsungan = input("\nMau Lanjut Apa Tidak? : ")
            clear()
            if keberlangsungan == "Lanjut":
                print("Program Akan Berjalan Kembali Dalam Waktu 5 detik")
                time.sleep(5)
            else:
                print("Terimakasih Telah Menggunakan Program Ini!")
                exit()
        else:
            print("Pilihan Menu Tidak Tersedia!")

    elif pilihan_program == "2":
        clear()
        print("Anda Memilih Persegi Panjang!")
        print(" 1. Luas?\n 2. Keliling?")
        pilihan_menu = input("Mau Menu Apa? : ")
        if pilihan_menu == "1":
            clear()
            print("Anda Memilih Luas")
            panjang = float(input("Masukkan Panjang dari Persegi Panjang yang Mau Anda Hitung! : "))
            clear()
            lebar = float(input("Masukkan Lebar dari Persegi Panjang yang Mau Anda Hitung! : "))
            clear()
            luas_persegiPanjang = panjang * lebar
            print(f"Luas Persegi Panjang Anda adalah {luas_persegiPanjang} cm\u00B2")
            keberlangsungan = input("\nMau Lanjut Apa Tidak? : ")
            clear()
            if keberlangsungan == "Lanjut":
                print("Program Akan Berjalan Kembali Dalam Waktu 5 detik")
                time.sleep(5)
            else:
                print("Terimakasih Telah Menggunakan Program Ini!")
                exit()
        elif pilihan_menu == "2":
            clear()
            print("Anda Memilih Keliling")
            panjang = float(input("Masukkan Panjang dari Persegi Panjang yang Mau Anda Hitung! : "))
            clear()
            lebar = float(input("Masukkan Lebar dari Persegi Panjang yang Mau Anda Hitung! : "))
            clear()
            keliling_persegiPanjang = 2 * (panjang + lebar)
            print(f"Keliling Persegi Panjang Anda adalah {keliling_persegiPanjang} cm\u00B2")
            keberlangsungan = input("\nMau Lanjut Apa Tidak? : ")
            clear()
            if keberlangsungan == "Lanjut":
                print("Program Akan Berjalan Kembali Dalam Waktu 5 detik")
                time.sleep(5)
            else:
                print("Terimakasih Telah Menggunakan Program Ini!")
                exit()
        else:
            print("Pilihan Menu Tidak Tersedia")

    elif pilihan_program == "3":
        clear()
        print("Anda Memilih Segitiga!")
        print(" 1. Luas?\n 2. Keliling?")
        pilihan_menu = (input("Mau Menu Apa? : "))
        if pilihan_menu == "1":
            alas = float(input("Masukkan Alas dari Segitiga yang Mau Anda Hitung : "))
            tinggi = float(input("Masukkan Tinggi dari Segitiga yang Mau Anda Hitung : "))
            luas_segitiga = alas * tinggi / 2
            print(f"Luas Segitiga Anda adalah {luas_segitiga} cm\u00B2")
            keberlangsungan = input("\nMau Lanjut Apa Tidak? : ")
            clear()
            if keberlangsungan == "Lanjut":
                print("Program Akan Berjalan Kembali Dalam Waktu 5 detik")
                time.sleep(5)
            else:
                print("Terimakasih Telah Menggunakan Program Ini!")
                exit()
        elif pilihan_menu == "2":
            alas = float(input("Masukkan Alas dari Segitiga yang Mau Anda Hitung : "))
            sisikiri = float(input("Masukkan Sisi Kiri dari Segitiga yang Mau Anda Hitung : "))
            sisikanan = float(input("Masukkan Sisi Kanan dari Segitiga yang Mau Anda Hitung : "))
            keliling_segitiga = alas + sisikiri + sisikanan
            print(f"Keliling Segitiga Anda adalah {keliling_segitiga} cm\u00B2")
            keberlangsungan = input("\nMau Lanjut Apa Tidak? : ")
            clear()
            if keberlangsungan == "Lanjut":
                print("Program Akan Berjalan Kembali Dalam Waktu 5 detik")
                time.sleep(5)
            else:
                print("Terimakasih Telah Menggunakan Program Ini!")
                exit()
        else:
            "Pilihan Menu Tidak Tersedia!"

    elif pilihan_program == "4":
        clear()
        print("Anda Memilih Lingkaran!")
        print(" 1. Luas?\n 2. Keliling?")
        pilihan_menu = (input("Mau Menu Apa? : "))
        if pilihan_menu == "1":
            clear()
            print("Anda Memilih Luas!")
            jari_jari = float(input("Masukkan Jari-Jari dari Lingkaran yang Mau Anda Hitung! : "))
            if jari_jari % 7 == 0:
                clear()
                luas_lingkaran = 22/7 * jari_jari ** 2
                print(f"Luas Lingkaran Anda adalah {luas_lingkaran} cm \u00B2")
            else:
                clear()
                luas_lingkaran = 3.14 * jari_jari ** 2
                print(f"Luas Lingkaran Anda adalah {luas_lingkaran} cm\u00B2")
            keberlangsungan = input("\nMau Lanjut Apa Tidak? : ")
            clear()
            if keberlangsungan == "Lanjut":
                print("Program Akan Berjalan Kembali Dalam Waktu 5 detik")
                time.sleep(5)
            else:
                print("Terimakasih Telah Menggunakan Program Ini!")
                exit()
        elif pilihan_menu == "2":
            clear()
            print("Anda Memilih Keliling")
            jari_jari = float(input("Masukkan Jari-Jari dari Lingkaran yang Mau Anda Hitung! : "))
            if jari_jari % 7 == 0:
                clear()
                keliling_lingkaran = 22/7 * 2 * jari_jari
                print(f"Keliling Lingkaran Anda adalah {keliling_lingkaran} cm \u00B2")
            else:
                clear()
                keliling_lingkaran = 3.14 * 2 * jari_jari
                print(f"Keliling Lingkaran Anda adalah {keliling_lingkaran} cm\u00B2")
                keberlangsungan = input("\nMau Lanjut Apa Tidak? : ")
            clear()
            if keberlangsungan == "Lanjut":
                print("Program Akan Berjalan Kembali Dalam Waktu 5 detik")
                time.sleep(5)
            else:
                print("Terimakasih Telah Menggunakan Program Ini!")
                exit()
        else:
            print("Pilihan Menu Ini Tidak Tersedia!")
    elif pilihan_program == "5":
        clear()
        print("Anda Keluar Dari Program. Terimakasih Telah Menggunakan Program Ini!")
        exit()
    else:
        clear()
        print("Maaf, Pilihan Program Ini Tidak Tersedia! Program Akan Berjalan Kembali dalam Waktu 5 detik")
        time.sleep(5)