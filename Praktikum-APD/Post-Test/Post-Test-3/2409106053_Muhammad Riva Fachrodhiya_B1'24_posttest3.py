import os
import math
# biar dapat nilai +
# Ngosongin Terminal
os.system('cls')

print("=" * 75)
print("         Menu Program Menghitung Luas/Keliling dari Bangun Datar")
print("=" * 75)
print("""\nMenu:
1. Persegi
2. Persegi Panjang
3. Segitga
4. Lingkaran\n""")
print("=" * 75)
pilihan_program = input("Mau Pilih Program Apa? (Masukkan Pilihan Program Anda dengan Angka)  ")
print("=" * 75)

os.system('cls')

if pilihan_program == "1":
   print("=" * 75)
   pilihan_menu = input("""Mau Luas Persegi atau Keliling Persegi? 
        1. Luas
        2. Keliling 
        (Masukkan Pilihan Menu Anda dengan Angka)  """)
   print("=" * 75)
   if pilihan_menu == "1":
      print("Anda Memilih Luas Persegi")
      sisi = float(input("Masukkan Nilai dari Sisi Persegi yang Mau Anda Hitung : "))
      luas_persegi = (sisi ** 2)
      print("Luas Persegi Anda adalah : ")
      print(f"{luas_persegi} cm\u00B2")
   elif pilihan_menu == "2":
      print("Anda Memilih Keliling Persegi")
      sisi = float(input("Masukkan Nilai dari Sisi Persegi yang Mau Anda Hitung : "))
      keliling_persegi = (4 * sisi)
      print("Keliling Persegi Anda adalah : ")
      print(keliling_persegi)
   else:
      print("Mohon Maaf, Terjadi Error, Tolong Jalankan Kembali Program Ini!")
elif pilihan_program == "2":
   print("=" * 75)
   pilihan_menu = input("""Mau Luas Persegi Panjang atau Keliling Persegi Panjang?
    1. Luas Persegi Panjang
    2. Keliling Persegi Panjang
    (Masukkan Pilihan Menu Anda dengan Angka)  """)
   print("=" * 75)
   if pilihan_menu == "1":
      print("Anda Memilih Luas Persegi Panjang")
      panjang = float(input("Masukkan Panjang dari Persegi Panjang yang Mau Anda Hitung : "))
      lebar = float(input("Masukkan Lebar dari Persegi Panjang yang Mau Anda Hitung : "))
      luas_persegiPanjang = panjang * lebar
      print("Luas Persegi Panjang Anda adalah : ")
      print(f"{luas_persegiPanjang} cm\u00B2")
   elif pilihan_menu == "2":
    print("Anda Memilih Keliling Persegi Panjang")
    panjang = float(input("Masukkan Panjang dari Persegi Panjang yang Mau Anda Hitung : "))
    lebar = float(input("Masukkan Lebar dari Persegi Panjang yang Mau Anda Hitung : "))
    keliling_persegiPanjang = 2 * (panjang + lebar)
    print("Keliling Persegi Panjang Anda adalah : ")
    print(keliling_persegiPanjang)
   else:
      print("Mohon Maaf, Terjadi Error, Tolong Jalankan Kembali Program Ini!")
elif pilihan_program == "3":
   print("=" * 75)
   pilihan_menu = input("""Mau Luas Segitiga atau Keliling Segitiga?
    1. Luas Segitiga
    2. Keliling Segitiga
    (Masukkan Pilihan Menu Anda dengan Angka)  """)
   print("=" * 75)
   if pilihan_menu == "1":
      print("Anda Memilih Luas Segitiga")
      alas = float(input("Masukkan Alas dari Segitiga yang Mau Anda Hitung : "))
      tinggi = float(input("Masukkan Tinggi dari Segitiga yang Mau Anda Hitung : "))
      luas_segitiga = alas * tinggi / 2
      print("Luas Segitiga Anda adalah : ")
      print(f"{luas_segitiga} cm\u00B2")
   elif pilihan_menu == "2":
    print("Anda Memilih Keliling Segitiga")
    alas = float(input("Masukkan Alas dari Segitiga yang Mau Anda Hitung : "))
    sisi_kiri = float(input("Masukkan Sisi Kiri dari Segitiga yang Mau Anda Hitung : "))
    sisi_kanan = float(input("Masukkan Sisi Kanan dari Segitiga yang Mau Anda Hitung : "))
    keliling_segitiga = alas + sisi_kiri + sisi_kanan
    print("Keliling Segitiga Anda adalah : ")
    print(keliling_segitiga)
   else:
      print("Mohon Maaf, Terjadi Error, Tolong Jalankan Kembali Program Ini!")
elif pilihan_program == "4":
   pilihan_menu = input("""Mau Luas Lingkaran atau Keliling Lingkaran?
    1. Luas Lingkaran
    2. Keliling Lingkaran
    (Masukkan Pilihan Menu Anda dengan Angka)  """)
   print("=" * 75)
   if pilihan_menu == "1":
      print("=" * 75)
      print("\nAnda Memilih Luas Lingkaran")
      jari_jari = float(input("Masukkan Jari-Jari Lingkaran yang Mau Anda Hitung : "))
      if jari_jari % 7 == 0:
         luas_lingkaran = 22/7 * jari_jari ** 2
      else:
         luas_lingkaran = 3.14 * jari_jari ** 2
      print("Luas Lingkaran Anda adalah : ")
      print(f"{luas_lingkaran} cm\u00B2")
   elif pilihan_menu == "2":
      print("Anda Memilih Keliling Lingkaran")
      jari_jari = float(input("Masukkan Jari-Jari Lingkaran yang Mau Anda Hitung : "))
      if jari_jari % 7 == 0:
         keliling_lingkaran = 2 * 22/7 * jari_jari
      else:
         keliling_lingkaran = 2 * 3.14 * jari_jari
      print("Keliling Lingkaran Anda adalah : ")
      print(keliling_lingkaran)
   else:
      print("Mohon Maaf, Terjadi Error, Tolong Jalankan Kembali Program Ini!")
else:
   print("Anda Keluar dari Program, Silahkan Jalankan Kembali")
print("\nTerima Kasih Sudah Menggunakan Program Ini!")
print("=" * 75)

