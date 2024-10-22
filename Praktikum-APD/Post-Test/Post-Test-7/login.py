from programcrud import loading,clear
akun = {
    "Owner": {"password": "Owner123", "role": "Owner"},
}

#bagian untuk login
def login():
    while True:
        try:
            print("=== SILAHKAN LOGIN ===")
            username = input("Masukkan username : ")
            password = input("Masukkan password : ") 

            if username in akun and akun[username]["password"] == password:
                print("Sedang memproses login . . .")
                loading(30,2.5)
                clear()
                print(f"Selamat datang, {username}!")
                input("Tekan Enter untuk melanjutkan.....")
                return akun[username]["role"], username  # Kembalikan role dan username
            else:
                print("Login gagal, Username atau Password salah! silakan coba lagi.")
            return None
        except Exception as e:
            print(f"Terjadi kesalahan saat login: {str(e)}")



# Bagian untuk registrasi
def registrasi():
    try:
        print("=== SILAHKAN REGISTRASI ===")
        username = input("Masukkan username anda: ")

        # Cek apakah username sudah ada
        if username in akun:
            print("Username sudah digunakan!")
            return

        password = input("Masukkan password anda: ")
        akun[username] = {"password": password, "role": "Admin"}
        print("Sistem sedang memproses. . . . ")

    except Exception as e:
        print(f"Terjadi kesalahan saat registrasi: {str(e)}")
