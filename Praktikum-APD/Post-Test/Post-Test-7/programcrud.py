import time
import os

def loading(panjangLoading=30, waktu=5):
    for i in range(panjangLoading + 1):
        time.sleep(waktu / panjangLoading)  
        bar = "=" * i + "-" * (panjangLoading - i)  
        print(f"\r[{bar}] {i * 100 // panjangLoading}%", end="")

def clear():
    os.system('cls||clear')

def lanjut():
    input("Tekan Enter untuk melanjutkan. . . .")

# Produk-produk ATK
produkATK = {
    1: {"nama": "Kertas Folio", "harga_jual": 1000, "stok": 100, "harga_beli": 500},
    2: {"nama": "Keras HVS", "harga_jual": 1000, "stok": 500, "harga_beli": 500},
    3: {"nama": "Buku Tulis", "harga_jual": 3000, "stok": 120, "harga_beli": 2000},
    4: {"nama": "Pensil", "harga_jual": 2000, "stok": 50, "harga_beli": 1000},
    5: {"nama": "Pulpen", "harga_jual": 2000, "stok": 50, "harga_beli": 1000},
}


# Tampilan Produk dengan Role Owner
def displayprodukOwner():
    print("\t\t\t\t ----- DAFTAR PRODUK -----")
    print("=" * 90)
    print(f"{'NO':<5}{'Nama':<20}{'Harga Jual':<15}{'Stok':<10}{'Harga Beli':<15}{'Profit':<15}")
    print("=" * 90)

    for no, produk in produkATK.items():
        profit = produk['harga_jual'] - produk['harga_beli']  # Menghitung profit per produk
        print(f"{no:<5}{produk['nama']:<20}{produk['harga_jual']:<15}{produk['stok']:<10}{produk['harga_beli']:<15}{profit:<15}")

    print("=" * 90)


# Tampilan Produk dengan Role Admin
def displayprodukAdmin():
    print("\t\t\t----- DAFTAR PRODUK -----")
    print("=" * 75)
    print(f"{'NO':<5}{'Nama':<20}{'Harga Jual':<15}{'Stok':<10}{'Harga Beli':<15}")
    print("=" * 75)

    for no, produk in produkATK.items():
        print(f"{no:<5}{produk['nama']:<20}{produk['harga_jual']:<15}{produk['stok']:<10}{produk['harga_beli']:<15}")
    print("=" * 75)

# BagianTambah Produk 
def TambahProduk():
    try:
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
    except Exception as e:
            print(f"Terjadi kesalahan: {(e)}")


# Bagian Update Produk
def updateProduk():
    try:
        displayprodukOwner()
        print("=" * 90)
        print("\t\t\t\t----- UPDATE PRODUK -----")
        print("=" * 90)
        no = int(input("Masukkan nomor produk yang ingin di-update: "))

        if no in produkATK:
            print(f"Produk ditemukan: {produkATK[no]['nama']}")
            produkATK[no]["nama"] = input("Masukkan nama produk baru: ")
            produkATK[no]["harga_jual"] = int(input("Masukkan harga jual baru: "))
            produkATK[no]["stok"] = int(input("Masukkan stok baru: "))
            produkATK[no]["harga_beli"] = int(input("Masukkan harga beli baru: "))
            print("Produk sedang di-update! Mohon tunggu dalam waktu 5 detik!")
            time.sleep(5)
            print("Produk berhasil di-update")
        else:
            print("Produk tidak ditemukan!")
    except Exception as e:
            print(f"Terjadi kesalahan: {(e)}")


# Bagian Hapus Produk
def hapusProduk():
    try:
        displayprodukOwner()
        print("=" * 90)
        print("\t\t\t\t----- HAPUS PRODUK -----")
        print("=" * 90)
        no = int(input("Masukkan nomor produk yang ingin dihapus: "))

        if no in produkATK:
            del produkATK[no]
            print("Produk berhasil dihapus!")
        else:
            print("Produk tidak ditemukan!")
    except Exception as e:
            print(f"Terjadi kesalahan: {(e)}")

# Bagian Total Profit
def profitKotor():
    totalProfit = 0
    for produk in produkATK.values():
        kotor = (produk["harga_jual"] - produk["harga_beli"]) * produk["stok"]
        totalProfit += kotor
    return totalProfit

def hitungPajak(totalProfit):
    if totalProfit() < 500000:
        return 0.10
    elif totalProfit() > 500000 and totalProfit() < 850000:
        return 0.15
    elif totalProfit() > 1000000:
        return 0.25
    return 0

def displayPajak(profitKotor):
    pajak = hitungPajak(profitKotor)
    print(f"Total pajak yang harus anda bayar adalah sebesar {pajak * 100}%")
    return pajak

def profitBersih():
    total = displayPajak(profitKotor) * profitKotor()
    profit = profitKotor() - total
    print(f"Total profit anda adalah sebesar Rp{profit}")

def ownerMenu(role = "Owner"):
    try:
        while True:
            clear()
            print("\t======================================================================================================")
            print(f"\t\t\t\t\t\t----- Menu {role.title()} -----")
            print("\t======================================================================================================")
            print("\t[1]\t\t\t\t\t    Lihat Produk\n\t[2]\t\t\t\t\t    Tambah Produk\n\t[3]\t\t\t\t\t    Update Produk\n\t[4]\t\t\t\t\t    Hapus Produk\n\t[5]\t\t\t\t\t    Lihat Profit\n\t[0]\t\t\t\t\t\tLogout")
            print("\t======================================================================================================")
            pilihanMenu = input("\t\t\t\t\t\t   Pilih menu : ")
            clear()
            loading(30,0.5)
            if pilihanMenu == "1":
                clear()
                displayprodukOwner()
                lanjut()
            elif pilihanMenu == "2":
                clear()
                TambahProduk()
                lanjut()
            elif pilihanMenu == "3":
                clear()
                updateProduk()
                lanjut()
            elif pilihanMenu == "4":
                clear()
                hapusProduk()
                lanjut()
            elif pilihanMenu == "5":
                while True:
                    clear()
                    print("1. Lihat Profit Kotor\n2. Lihat Pajak\n3. Lihat Profit Bersih\n0. Keluar")
                    pilihanProfit = input("Masukkan pilihan anda: ")
                    if pilihanProfit == "1":
                        clear()
                        profit = print(f"Profit kotor anda adalah sebesar Rp{profitKotor()}")
                        lanjut()
                    elif pilihanProfit == "2":
                        clear()
                        displayPajak(profitKotor)
                        lanjut()
                    elif pilihanProfit == "3":
                        clear()
                        profitBersih()
                        lanjut()
                    elif pilihanProfit == "0":
                        break
                    else:
                        print("Pilihan anda tidak valid!")
                        lanjut()

            elif pilihanMenu == "0":
                clear()
                print("Anda telah logout dari program!")
                lanjut()
                break
    except Exception as e:
        print(f"Terjadi kesalahan: {(e)}")


def adminMenu(role = "Admin"):
    try:
        while True:
            clear()
            print("\t======================================================================================================")
            print(f"\t\t\t\t\t\t----- Menu Admin -----")
            print("\t======================================================================================================")
            print("\t[1].\t\t\t\t\t   Lihat Produk\n\t[2].\t\t\t\t\t   Tambah Produk\n\t[3].\t\t\t\t\t   Update Produk\n\t[0].\t\t\t\t\t      Logout")
            print("\t======================================================================================================")
            pilihanMenu = input("\t\t\t\t\t\t   Pilih menu : ")

            if pilihanMenu == "1":
                clear()
                displayprodukAdmin()
                lanjut()
            elif pilihanMenu == "2":
                clear()
                TambahProduk()
                lanjut()
            elif pilihanMenu == "3":
                clear()
                updateProduk()
                lanjut()
            elif pilihanMenu == "0":
                clear()
                print("Anda telah logout dari program!")
                loading(30,2.5)
                print()
                lanjut()
                break
    except Exception as e:
            print(f"Terjadi kesalahan: {(e)}")
 