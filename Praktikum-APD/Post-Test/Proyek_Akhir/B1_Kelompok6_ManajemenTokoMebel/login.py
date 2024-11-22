import json
import re
import shutil
import os
from CRUD import lanjut,inputTengah,print_tengah
from menu import tampilkanMenuBiasa
# Fungsi untuk membersihkan layar
def clear():
    os.system('cls||clear')
# Fungsi untuk membaca data pengguna dari file JSON
def bacaUser():
    if not os.path.exists('datausername.json'):
        raise FileNotFoundError("Data user tidak ditemukan")
    with open('datausername.json', 'r') as file:
        return json.load(file)

# Fungsi untuk menulis data pengguna ke file JSON
def daftarUser(datauser):
    with open('datausername.json', 'w') as file:
        json.dump(datauser, file, indent=4)

# Validasi username
def cekUsername(username):
    if not username:
        raise ValueError("Username tidak boleh kosong.")
    if not re.match("^[A-Za-z0-9]*$", username):
        raise ValueError("Username tidak boleh menggunakan karakter spesial.")
    if not any(char.isdigit() for char in username):
        raise ValueError("Username harus mengandung minimal 1 angka.")
    if not any(char.isupper() for char in username):
        raise ValueError("Username harus mengandung minimal 1 huruf kapital.")

# Validasi password
def cekPassword(password):
    if not password:
        raise ValueError("Password tidak boleh kosong.")
    if len(password) <= 5:
        raise ValueError("Password harus lebih dari 5 karakter.")
    if not re.match("^[A-Za-z0-9]*$", password):
        raise ValueError("Password tidak boleh menggunakan karakter spesial.")
    if not any(char.isdigit() for char in password):
        raise ValueError("Password harus mengandung minimal 1 angka.")
    if not any(char.isupper() for char in password):
        raise ValueError("Password harus mengandung minimal 1 huruf kapital.")

# Membaca data pengguna
datauser = bacaUser()

# Fungsi login
def login():
    while True:
        datauser = bacaUser()
        clear()  # Pastikan fungsi clear() didefinisikan
        tampilkanMenuBiasa("LOGIN")  # Pastikan fungsi ini didefinisikan
        username = input("\t\t\t\t\t\t\t\t\t\t\t   Username -> ").strip()
        password = input("\t\t\t\t\t\t\t\t\t\t\t   Password -> ").strip()
        
        try:
            # Validasi username dan password
            cekUsername(username)
            cekPassword(password)

            # Cek apakah username ada di datauser dan password sesuai
            akun = next((item for item in datauser["akun"] if item["username"] == username), None)
            if akun and akun['password'] == password:
                clear()
                print_tengah(f"Akun Anda berhasil login dengan ID: {username} sebagai {akun['role']}.")
                print_tengah("Tekan enter untuk melanjutkan. . . . . ")
                input("")
                return akun
            else:
                clear()
                print_tengah("Username atau password salah.")
                lanjut()

        except ValueError as e:
            print(e)
            lanjut()