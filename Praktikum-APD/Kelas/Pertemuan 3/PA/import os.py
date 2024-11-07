import os
import re

def clear():
    os.system('cls||clear')

akun = {
    "Owner": {"password": "Ownertokomebel66", "role": "Owner"},
}
# Contoh string
teks = "Hello, World! Ini contoh teks dengan karakter spesial: @#$%^&*()"

# Pola untuk mendeteksi karakter spesial
pola = r"[^\w\s]"

# Mencari karakter spesial dalam string
karakter_spesial = re.findall(pola, teks)

if karakter_spesial:
    print("Karakter spesial terdeteksi:")
    print(karakter_spesial)
else:
    print("Tidak ada karakter spesial yang ditemukan.")

def is_valid_username(username):
    """Check if the username is valid: not empty and contains no special characters."""
    any(char.isupper() for char in username) and any(char.isalpha() for char in username) and any(char.strip() for char in username)
    return username

def is_valid_password(password):
    """Check if the password is valid: not empty, contains at least one uppercase letter, and no special characters."""
    any(char.isupper() for char in password) and any(char.isalpha() for char in password) and any(char.strip() for char in password)
    return password

def login():
    while True:
        try:
            print("=== SILAHKAN LOGIN ===")
            username = input("Masukkan username : ").strip()
            password = input("Masukkan password : ").strip()

            # Validate username and password
            if not is_valid_username(username):
                print("Error: Username tidak boleh kosong dan tidak boleh mengandung karakter spesial!")
                continue
            
            if not is_valid_password(password):
                print("Error: Password harus mengandung setidaknya satu huruf kapital dan tidak boleh mengandung karakter spesial!")
                continue

            if username in akun and akun[username]["password"] == password:
                print("Sedang memproses login . . .")
                print(f"Selamat datang, {username}!")
                input("Tekan Enter untuk melanjutkan.....")
                return akun[username]["role"], username  # Kembalikan role dan username
            else:
                print("Login gagal, Username atau Password salah! Silakan coba lagi.")
        
        except Exception as e:
            print(f"Terjadi kesalahan saat login: {str(e)}")

def registrasi():
    while True:
        try:
            print("=== SILAHKAN REGISTRASI ===")
            username = input("Masukkan username anda: ").strip()

            # Validate username
            if not is_valid_username(username):
                print("Error: Username tidak boleh kosong dan tidak boleh mengandung karakter spesial!")


            # Cek apakah username sudah ada
            if username in akun:
                print("Username sudah digunakan!")

            password = input("Masukkan password anda: ").strip()

            # Validate password
            if not is_valid_password(password):
                print("Error: Password harus mengandung setidaknya satu huruf kapital dan tidak boleh mengandung karakter spesial!")

            akun[username] = {"password": password, "role": "Admin"}
            print("Sistem sedang memproses. . . . ")
        
        except Exception as e:
            print(f"Terjadi kesalahan saat registrasi: {str(e)}")

clear()
login()