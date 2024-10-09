#CRUD "Manajemen Keuntungan dari Suatu Perusahaan ATK"
import os
import time
clear = lambda: os.system('cls || clear')
clear()

#Pengguna akun dengan format (username, password, role)

akun = [
    ["Owner", "Owner123", "Owner"],
]

#Produk-produk ATK dengan format (no, barang, harga jual, stok , harga beli)

produkATK = [
    [1, "Kertas Folio", 1000, 100, 500,],
    [2, "Keras HVS \t", 1000, 500, 500],
    [3, "Buku Tulis", 3000, 120, 2000],
    [4, "Pensil", 2000, 50, 1000],
    [5, "Pulpen", 2000, 50, 1000],
]


#Bagian untuk login
def login():
    clear()
    while True:
        print("=== SILAHKAN LOGIN ===")
        username = (input("Masukkan username : "))
        password = input("Masukkan password : ") 

        for user in akun:
            if user[0] == username and user[1] == password:
                print("Anda berhasil login!")
                input("Tekan Enter untuk melanjutkan.....")
                return user[2] #Buat kasih role
        print("Username atau Password salah!")
        print()
        input("Tekan Enter untuk melanjutkan....")
        clear()

#Bagian untuk regis
def registrasi():
    clear()
    try:
        print("=== SILAHKAN REGISTRASI ===")
        username = input("Masukkan username anda: ")
        
        # Cek apakah username sudah ada
        for user in akun:
            if user[0] == username:
                print("Username sudah digunakan!")
                return
            password = input("Masukkan password anda: ")
            akun.append([username, password, "Admin"])
            print("Registrasi berhasil! Silahkan kembali login!")
            input("Tekan Enter untuk melanjutkan.....")
            return
    except Exception as e:
        print(f"Terjadi kesalahan saat registrasi: {str(e)}")

#Tampilan Produk Owner
def displayprodukOwner():
    clear()
    print("\t\t\t----- DAFTAR PRODUK -----")
    print("=" * 75)
    print(f"{'NO':<5}{'Nama':<20}{'Harga Jual':<15}{'Stok':<10}{'Harga Beli':<15}{'Profit':<10}")
    for produk in produkATK:
        profit = produk[2] - produk[4]
        print(f"{produk[0]:<5}{produk[1]:<20}{produk[2]:<15}{produk[3]:<10}{produk[4]:<15}{profit:<10}")
    print("=" * 75)

#Tampilan Produk Admin
def displayprodukAdmin():
    clear()
    print("\t\t\t----- DAFTAR PRODUK -----")
    print("=" * 75)
    print(f"{'NO':<5}{'Nama':<20}{'Harga Jual':<15}{'Stok':<10}{'Harga Beli':<15}")
    for produk in produkATK:
        print(f"{produk[0]:<5}{produk[1]:<20}{produk[2]:<15}{produk[3]:<10}{produk[4]:<15}")
    print("=" * 75)

#Tambah Produk
def TambahProduk():
    clear()
    try:
        print("=== TAMBAH PRODUK ===")
        barang = input("Masukkan nama produk: ")
        hargaBeli = int(input("Masukkan harga beli: "))
        hargaJual = int(input("Masukkan harga jual: "))
        stok = int(input("Masukkan jumlah stok: "))
        
        nomorBaru = max([p[0] for p in produkATK]) + 1
        produkATK.append([nomorBaru, barang, hargaJual, stok, hargaBeli])
        print("Produk berhasil ditambahkan!")
    except ValueError:
        print("Mohon masukkan angka yang valid untuk harga dan stok!")
    except Exception as e:
        print(f"Terjadi kesalahan: {(e)}")

#Update Produk
def updateProduk():
    clear()
    try:
        displayprodukAdmin()
        idProduk = int(input("\nMasukkan ID produk yang akan diupdate: "))
        
        for produk in produkATK:
            if produk[0] == idProduk:
                print(f"Mengupdate produk: {produk[1]}")
                produk[1] = input("Masukkan nama baru (kosongkan jika tidak diubah): ") or produk[1]
                produk[2] = int(input("Masukkan harga beli baru (0 jika tidak diubah): ")) or produk[2]
                produk[3] = int(input("Masukkan stok baru (0 jika tidak diubah): ")) or produk[3]
                produk[4] = int(input("Masukkan harga jual baru (0 jika tidak diubah): ")) or produk[4]
                clear()
                print("Produk sedang diupdate! Mohon tunggu 5 detik.....")
                time.sleep(5)
                clear()
                input("Tekan Enter untuk melanjutkan.....")
                clear()
                displayprodukAdmin()
                return
        print("ID produk tidak ditemukan!")
    except ValueError:
        print("Mohon masukkan ID yang valid!")
    except Exception as e:
        print(f"Terjadi kesalahan: {str(e)}")

#Hapus Produk
def hapusProduk():
    clear()
    try:
        displayprodukOwner()
        idProduk = int(input("\nMasukkan nomor produk yang akan dihapus: "))
        
        for produk in produkATK:
            if produk[0] == idProduk:
                produkATK.remove(produk)
                clear()
                print("Produk sedang dihapus! Mohon tunggu 5 detik.....")
                time.sleep(5)
                input("Produk berhail dihapus! Tekan Enter untuk melanjutkan.....")
                clear()
                displayprodukOwner()
                return
        print("ID produk tidak ditemukan!")
    except ValueError:
        print("Mohon masukkan ID yang valid!")
    except Exception as e:
        print(f"Terjadi kesalahan: {str(e)}")

#Total profit
def totalProfit():
    total_profit = 0
    for produk in produkATK:
        # harga jual - harga beli
        profitPcs = produk[2] - produk[4]
        # profit per pieces dikali stok produk
        total_profit += profitPcs * produk[3]
    return total_profit
def main():
    while True:
        clear()
        print("=" * 75)
        print("\tPROGRAM MANAJEMEN KEUNTUNGAN DARI SUATU PERUSAHAAN ATK")
        print("=" * 75)
        print("[1] Login\n[2] Register\n[3] Keluar Program")
        print("=" * 75)

        pilihan = input("Pilih Menu (1-3): ")
        
        if pilihan == "1":
            role = login()
            while True:
                clear()
                if role == "Owner":
                    print(f"=== Menu {role.title()} ===")
                    print("1. Lihat Produk\n2. Tambah Produk\n3. Update Produk\n4. Hapus Produk\n5. Lihat Profit\n0. Logout")
                    pilihanMenu = input("Pilih menu : ")
                    
                    if pilihanMenu == "1":
                        clear()
                        displayprodukOwner()
                        input("Tekan Enter untuk kembali ke menu...")
                    elif pilihanMenu == "2":
                        clear()
                        TambahProduk()
                        input("Tekan Enter untuk kembali ke menu...")
                    elif pilihanMenu == "3":
                        clear()
                        updateProduk()
                        input("Tekan Enter untuk kembali ke menu...")
                    elif pilihanMenu == "4":
                        clear()
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
                    clear()
                    print(f"=== Menu {role.title()} ===")
                    print("1. Lihat Produk\n2. Tambah Produk\n3. Update Produk\n0. Logout")
                    pilihanMenu = input("Pilih menu : ")
                    
                    if pilihanMenu == "1":
                        clear()
                        displayprodukAdmin()
                        input("Tekan Enter untuk kembali ke menu...")
                    elif pilihanMenu == "2":
                        clear()
                        TambahProduk()
                        input("Tekan Enter untuk kembali ke menu...")
                    elif pilihanMenu == "3":
                        clear()
                        updateProduk()
                        input("Tekan Enter untuk kembali ke menu...")
                    elif pilihanMenu == "0":
                        clear
                        print("Anda telah logout dari program!")
                        input("Tekan Enter untuk melanjutkan.....")
                        break
                    
        elif pilihan == "2":
            registrasi()
        elif pilihan == "3":
            clear()
            print("Terima kasih telah menggunakan program ini!")
            exit()

                
                
main()