import json
import os
import re
import shutil
from CRUD import *
from menu import tampilkanMenuBiasa
# Fungsi untuk membaca data pengguna dari file JSON
def bacaUser():
    if not os.path.exists('datausername.json'):
        raise FileNotFoundError("Data user tidak ditemukan")
    with open('datausername.json', 'r') as file:
        return json.load(file)

# Fungsi untuk menambahkan data pengguna ke file JSON
def tambahUser(userData):
    if not os.path.exists('datausername.json'):
        raise FileNotFoundError("Data user tidak ditemukan")
    with open('datausername.json', 'r') as file:
        datauser = json.load(file)
    
    # Periksa apakah username sudah ada
    for user in datauser["akun"]:
        if user["username"] == userData["username"]:
            raise ValueError("\t\t\t\t\t\t\t\t\t\t\tUsername sudah ada. Silakan pilih username lain.")
    
    datauser["akun"].append(userData)
    
    with open('datausername.json', 'w') as file:
        json.dump(datauser, file, indent=4)

# Fungsi validasi username
def cekUsername(username):
    if not username:
        raise ValueError("\t\t\t\t\t\t\t\t\t\t\t\tUsername tidak boleh kosong.")
    if re.search(r'[^a-zA-Z0-9_]', username):
        raise ValueError("\t\t\t\t\t\t\t\t\t\t\t\tUsername tidak boleh mengandung karakter spesial.")
    if not username.strip():
        raise ValueError("\t\t\t\t\t\t\t\t\t\t\t\tUsername tidak boleh kosong")

# Fungsi validasi password
def cekPassword(password):
    if len(password) < 5:
        raise ValueError("Password harus memiliki minimal 5 karakter.")
    if not re.search(r'[A-Z]', password):
        raise ValueError("Password harus memiliki minimal satu huruf kapital.")
    if re.search(r'[^a-zA-Z0-9]', password):
        raise ValueError("Password tidak boleh mengandung karakter spesial.")

def register():
    while True:
        clear()
        tampilkanMenuBiasa("REGISTER")
        
        try:
            username = input("\t\t\t\t\t\t\t\t\t\t\tUsername -> ").strip()
            cekUsername(username)
            
            password = input("\t\t\t\t\t\t\t\t\t\t\tPassword -> ").strip()
            cekPassword(password)
            
            userBaru = {
                "username": username,
                "password": password,
                "role": "Pembeli",
                "saldo": 0,
                "riwayatPembelian":[]
            }
            tambahUser(userBaru)
            clear()
            print_tengah(f"Akun Anda berhasil terdaftar dengan ID: {username} sebagai Pembeli.")
            lanjut()
            clear()
            return
        except ValueError as e:
            clear()
            print(e)
            print_tengah("Tekan Enter untuk mengulang program. . .")
            input("")
        except EOFError:
            clear()
            print_tengah("Input dihentikan oleh pengguna. Program akan keluar.")
            break