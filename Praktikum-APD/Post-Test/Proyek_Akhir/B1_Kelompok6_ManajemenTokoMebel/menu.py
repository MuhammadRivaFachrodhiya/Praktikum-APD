from CRUD import *
from prettytable import PrettyTable
from tabulate import tabulate
import re
import shutil

def tampilkanMenuBiasa(kata):
    menu = PrettyTable()
    menu.field_names = [f">> MENU {kata} <<"]
    menu.padding_width = 19
    lebarTerminal = shutil.get_terminal_size().columns
    
    for line in menu.get_string().splitlines():
        print(line.center(lebarTerminal))

def tampilkanMenutama():
    menu = PrettyTable()
    menu.field_names = ["SELAMAT DATANG DI MENU UTAMA"] 
    menu.add_row(["1.Login"])
    menu.add_row(["2.Register"])
    menu.add_row(["0.Keluar"])
    
    menu.padding_width = 10
    menu.max_width = 20     
    lebarTerminal = shutil.get_terminal_size().columns
    for line in menu.get_string().splitlines():
        print(line.center(lebarTerminal))
    

def tampilkanPembeliMenu():
    menu = PrettyTable()
    menu.field_names = ["No", "Menu Toko Mebel"]
    menu.add_row(["1", "Lihat Produk"])
    menu.add_row(["2", "Beli Produk"])
    menu.add_row(["3", "Topup Saldo"])
    menu.add_row(["4", "Lihat Saldo"])
    menu.add_row(["5", "Lihat Riwayat Pembelian"])
    menu.add_row(["6", "Keluar"])
    
    menu.max_width["No"] = 5
    menu.max_width["Menu Toko Mebel"] = 25
    menu.padding_width = 2

    lebarTerminal = shutil.get_terminal_size().columns
    for line in menu.get_string().splitlines():
        print(line.center(lebarTerminal))
    

def tampilkanOwnerMenu():
    menu = PrettyTable()
    menu.field_names = ["No", "Menu Toko Mebel"]
    menu.add_row(["1", "Tambah Produk"])
    menu.add_row(["2", "Lihat Produk"])
    menu.add_row(["3", "Update Produk"])
    menu.add_row(["4", "Hapus Produk"])
    menu.add_row(["5", "Lihat Profit"])
    menu.add_row(["6", "Keluar"])
    
    menu.padding_width = 15  
    menu.max_width = 20
    
    lebarTerminal = shutil.get_terminal_size().columns
    for line in menu.get_string().splitlines():
        print(line.center(lebarTerminal))

def ownerMenu():
    while True:
        clear()
        tampilkanOwnerMenu()
        try:
            choice = inputTengah("Pilih menu (1-6): ").strip()
            if not choice:
                raise ValueError("\t\t\t\t\t\t\t\t\t\t\t\tPilihan menu tidak boleh kosong.")
            if not re.match("^[A-Za-z0-9]*$", choice):
                raise ValueError("\t\t\t\t\t\t\t\t\t\t\tPilihan menu tidak boleh menggunakan karakter spesial.")
            if choice not in ["1","2","3","4","5","6"]:
                raise ValueError("\t\t\t\t\t\t\t\t\t\t\t  Pilihan harus di angka 1-6")
            if choice == '1':
                clear()
                loading()
                print("Selesai!")
                tambahProduk()
                lanjut()
            elif choice == '2':
                clear()
                loading()
                lanjut()
                clear()
                lihatProduk()
                lanjut()
            elif choice == '3':
                clear()
                updateProduk()
                lanjut()
            elif choice == '4':
                clear()
                hapusProduk()
                lanjut()
            elif choice == '5':
                clear()
                loading()
                lanjut()
                hitungProfit()
                lanjut()
            elif choice == '6':
                clear()
                print_tengah("Keluar dari program.")
                time.sleep(3)
                break
            else:
                print("Pilihan tidak valid.\n")
        except Exception as e:
           clear()
           print(e)
           lanjut()

def pembeliMenu(username):
    while True:
        clear()
        tampilkanPembeliMenu()
        try:
            choice = input("\t\t\t\t\t\t\t\t\t\t\t\t\t  Pilih menu: ").strip()
            if not choice:
                raise ValueError("\t\t\t\t\t\t\t\t\t\t\t\tPilihan menu tidak boleh kosong.")
            if not re.match("^[A-Za-z0-9]*$", choice):
                raise ValueError("\t\t\t\t\t\t\t\t\t\t\tPilihan menu tidak boleh menggunakan karakter spesial.")
            if choice not in ['0','1','2','3','4','5','6']:
                raise ValueError("\t\t\t\t\t\t\t\t\t\t\t     Pilihan menu harus berupa angka (0,1,2).")
            clear()
            if choice == '1':
                bacaUser()
                lihatProdukPembeli(username)
                lanjut()
            elif choice == '2':
                pembelian(username)
                lanjut()
            elif choice == '3':
                try:
                    jumlah = float(inputTengah("Berapa nominal yang mau anda topup : "))
                    if jumlah < 0:
                        print_tengah("Masukkan nominal diatas 0 rupiah.")
                        return
                    if isinstance(jumlah,int):
                        raise ValueError("\t\t\t\t\t\t\t\t\t\t\t\t\tNominal berupa angka")
                except Exception as e:
                    clear()
                    print(e)
                    time.sleep(3)
                jumlah_float = float(jumlah)
                topupSaldo(username,jumlah_float)
                lanjut()
            elif choice == '4':
                lihatSaldo(username)
                lanjut()
            elif choice == '5':
                tampilkanRiwayat(username)
                lanjut()
            elif choice == '6':
                break
        except Exception as e:
            clear()
            print(e)
            lanjut()