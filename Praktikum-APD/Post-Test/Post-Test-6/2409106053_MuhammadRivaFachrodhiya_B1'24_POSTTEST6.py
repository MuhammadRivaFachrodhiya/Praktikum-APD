# CRUD "Manajemen Keuntungan dari Suatu Perusahaan ATK"
import os
import time

clear = lambda: os.system('cls || clear')
clear()

# Pengguna akun dengan format username sebagai key, dan value-nya berupa dictionary dengan password dan role
akun = {
    "Owner": {"password": "Owner123", "role": "Owner"}
}

# Produk-produk ATK dengan nomor produk sebagai key, dan value-nya berupa dictionary dengan detail produk
produkATK = {
    1: {"nama": "Kertas Folio", "harga_jual": 1000, "stok": 100, "harga_beli": 500},
    2: {"nama": "Keras HVS", "harga_jual": 1000, "stok": 500, "harga_beli": 500},
    3: {"nama": "Buku Tulis", "harga_jual": 3000, "stok": 120, "harga_beli": 2000},
    4: {"nama": "Pensil", "harga_jual": 2000, "stok": 50, "harga_beli": 1000},
    5: {"nama": "Pulpen", "harga_jual": 2000, "stok": 50, "harga_beli": 1000},
}

# Bagian untuk login
def login():
    clear()
    while True:
        print("=== SILAHKAN LOGIN ===")
        username = input("Masukkan username : ")
        password = input("Masukkan password : ") 

        if username in akun and akun[username]["password"] == password:
            print("Anda berhasil login!")
            input("Tekan Enter untuk melanjutkan.....")
            return akun[username]["role"]  # Mengembalikan role
        else:
            print("Username atau Password salah!")
            print()
            input("Tekan Enter untuk melanjutkan....")
            clear()

# Bagian untuk registrasi
def registrasi():
    clear()
    try:
        print("=== SILAHKAN REGISTRASI ===")
        username = input("Masukkan username anda: ")

        # Cek apakah username sudah ada
        if username in akun:
            print("Username sudah digunakan!")
            return

        password = input("Masukkan password anda: ")
        akun[username] = {"password": password, "role": "Admin"}
        print("Registrasi berhasil! Silahkan kembali login!")
        input("Tekan Enter untuk melanjutkan.....")

    except Exception as e:
        print(f"Terjadi kesalahan saat registrasi: {str(e)}")

# Tampilan Produk dengan Role Owner
def displayprodukOwner():
    clear()
    print("\t\t\t\t ----- DAFTAR PRODUK -----")
    print("=" * 90)
    print(f"{'NO':<5}{'Nama':<20}{'Harga Jual':<15}{'Stok':<10}{'Harga Beli':<15}{'Profit':<15}")
    print("=" * 90)

    for no, produk in produkATK.items():
        profit = produk['harga_jual'] - produk['harga_beli']  # Menghitung profit per produk
        print(f"{no:<5}{produk['nama']:<20}{produk['harga_jual']:<15}{produk['stok']:<10}{produk['harga_beli']:<15}{profit:<15}")

    print("=" * 90)


# Tampilan Produk Admin
def displayprodukAdmin():
    clear()
    print("\t\t\t----- DAFTAR PRODUK -----")
    print("=" * 75)
    print(f"{'NO':<5}{'Nama':<20}{'Harga Jual':<15}{'Stok':<10}{'Harga Beli':<15}")
    print("=" * 75)

    for no, produk in produkATK.items():
        print(f"{no:<5}{produk['nama']:<20}{produk['harga_jual']:<15}{produk['stok']:<10}{produk['harga_beli']:<15}")
    print("=" * 75)

#  Tambah Produk 
def TambahProduk():
    clear()
    displayprodukOwner()
    print("=" * 90)
    print("\t\t\t\t ------ TAMBAH PRODUK -----")
    print("=" * 90)
    noBarang = int(input("Masukkan nomor produk: "))
    nama = input("Masukkan nama produk: ")
    harga_jual = int(input("Masukkan harga jual produk: "))
    stok = int(input("Masukkan stok produk: "))
    harga_beli = int(input("Masukkan harga beli produk: "))

    produkATK[noBarang] = {"nama": nama, "harga_jual": harga_jual, "stok": stok, "harga_beli": harga_beli}
    print("Produk berhasil ditambahkan!")

# Fungsi Update Produk
def updateProduk():
    clear()
    displayprodukOwner()
    print("=" * 75)
    print("\t\t\t----- UPDATE PRODUK -----")
    print("=" * 75)
    no = int(input("Masukkan nomor produk yang ingin di-update: "))

    if no in produkATK:
        print(f"Produk ditemukan: {produkATK[no]['nama']}")
        produkATK[no]["nama"] = input("Masukkan nama produk baru: ")
        produkATK[no]["harga_jual"] = int(input("Masukkan harga jual baru: "))
        produkATK[no]["stok"] = int(input("Masukkan stok baru: "))
        produkATK[no]["harga_beli"] = int(input("Masukkan harga beli baru: "))
        clear()
        print("Produk sedang di-update! Mohon tunggu dalam waktu 5 detik!")
        time.sleep(5)
        print("Produk berhasil di-update")
    else:
        print("Produk tidak ditemukan!")

# Fungsi Hapus Produk
def hapusProduk():
    clear()
    displayprodukOwner()
    print("=" * 75)
    print("\t\t\t----- HAPUS PRODUK -----")
    print("=" * 75)
    no = int(input("Masukkan nomor produk yang ingin dihapus: "))

    if no in produkATK:
        del produkATK[no]
        print("Produk berhasil dihapus!")
    else:
        print("Produk tidak ditemukan!")

# Fungsi Total Profit
def totalProfit():
    total_profit = 0
    for produk in produkATK.values():
        profit = (produk["harga_jual"] - produk["harga_beli"]) * produk["stok"]
        total_profit += profit
    return total_profit

# Main Menu
def main():
    while True:
        clear()
        print("=== Sistem Manajemen Keuntungan Perusahaan ATK ===")
        print("1. Login")
        print("2. Registrasi")
        print("3. Keluar")
        pilihan = input("Pilih menu : ")

        if pilihan == "1":
            role = login()
            if role == "Owner":
                while True:
                    clear()
                    print(f"=== Menu {role.title()} ===")
                    print("1. Lihat Produk\n2. Tambah Produk\n3. Update Produk\n4. Hapus Produk\n5. Lihat Total Profit\n0. Logout")
                    pilihanMenu = input("Pilih menu : ")

                    if pilihanMenu == "1":
                        displayprodukOwner()
                        input("Tekan Enter untuk kembali ke menu...")
                    elif pilihanMenu == "2":
                        TambahProduk()
                        input("Tekan Enter untuk kembali ke menu...")
                    elif pilihanMenu == "3":
                        updateProduk()
                        input("Tekan Enter untuk kembali ke menu...")
                    elif pilihanMenu == "4":
                        hapusProduk()
                        input("Tekan Enter untuk kembali ke menu...")
                    elif pilihanMenu == "5":
                        clear()
                        total_profit = totalProfit()
                        print(f"Total keuntungan anda sebesar Rp{total_profit}")
                        input("Tekan Enter untuk kembali ke menu...")
                    elif pilihanMenu == "0":
                        clear()
                        print("Anda telah logout dari program!")
                        input("Tekan Enter untuk melanjutkan.....")
                        break
            elif role == "Admin":
                while True:
                    clear()
                    print(f"=== Menu {role.title()} ===")
                    print("1. Lihat Produk\n2. Tambah Produk\n3. Update Produk\n0. Logout")
                    pilihanMenu = input("Pilih menu : ")

                    if pilihanMenu == "1":
                        displayprodukAdmin()
                        input("Tekan Enter untuk kembali ke menu...")
                    elif pilihanMenu == "2":
                        TambahProduk()
                        input("Tekan Enter untuk kembali ke menu...")
                    elif pilihanMenu == "3":
                        updateProduk()
                        input("Tekan Enter untuk kembali ke menu...")
                    elif pilihanMenu == "0":
                        clear()
                        print("Anda telah logout dari program!")
                        input("Tekan Enter untuk melanjutkan.....")
                        break
        elif pilihan == "2":
            registrasi()
        elif pilihan == "3":
            clear()
            print("Terima kasih telah menggunakan program ini! Program akan tertutup secara otomatis dalam 5 detik. . . .")
            time.sleep(5)
            exit()

main()
