import pandas as pd
from tabulate import tabulate
from datetime import datetime
import os 
import time
import shutil
import re
import json

# Biar input ditengah terminal
def inputTengah(kata):
    lebarTerminal = shutil.get_terminal_size().columns
    samping = (lebarTerminal - len(kata)) // 2
    print(" " * samping + kata, end="")
    
    userInput = input()
    return userInput

# Biar print ditengah terminal
def print_tengah(text):
    lebarTerminal = shutil.get_terminal_size().columns
    teks = text.center(lebarTerminal)
    print(teks)

# Biar delay program
def lanjut():
    print_tengah("Tekan Enter untuk melanjutkan. . . .")
    input("")

# Buat baca user di file JSON
def bacaUser():
    if not os.path.exists('datausername.json'):
        raise FileNotFoundError("Data user tidak ditemukan")
    with open('datausername.json', 'r') as file:
        return json.load(file)

# Buat save user di file JSON
def simpanUserData(data, file_path='datausername.json'):
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=4)

# Biar save data di file Excel
def simpanDataProduk(df):
    df.reset_index(drop=True, inplace=True)
    df['No'] = df.index + 1
    df = df[['No', 'Nama', 'Harga Beli', 'Stok', 'Harga Jual']]
    df.to_excel('produkk.xlsx', index=False)

# Buat ngebersihin terminal
def clear():
    os.system('cls||clear')

# Buat ngedelay program juga
def loading():
    terminal_width = shutil.get_terminal_size().columns
    teks = "Loading"
    for i in range(10):
        titik = "." * (i % 4)
        print(" " * ((terminal_width - len(teks + titik)) // 2) + teks + titik, end="\r")
        time.sleep(0.5)
    print(" " * terminal_width, end="\r")
    print(" " * ((terminal_width - len("Selesai")) // 2) + "Selesai")
    
# Membaca data dari file Excel
def loadData():
    try:
        df = pd.read_excel('produkk.xlsx')
        return df
    except FileNotFoundError:
        print("File tidak ditemukan. Pastikan file 'products.csv' berada di direktori yang benar.")
        return pd.DataFrame()

# 1. Melihat produk role Owner
def lihatProduk():
    df = loadData()
    
    tabel = tabulate(df, headers='keys', tablefmt='fancy_grid', showindex=False)
    lebarTerminal = shutil.get_terminal_size().columns
    samping = (lebarTerminal - len(tabel.splitlines()[0])) // 2
    for line in tabel.splitlines():
        print(" " * samping + line)
# Role Pembeli
def lihatProdukPembeli(username):
    df = loadData()
    data = bacaUser()

    akun = next((a for a in data['akun'] if a['username'] == username), None)
    if akun is None:
        print_tengah("Akun tidak ditemukan.")
        return
    
    if akun['role'] == "Pembeli":
        if "Harga Beli" in df.columns:
            df = df.drop(columns=["Harga Beli"])

    tabel = tabulate(df, headers='keys', tablefmt='fancy_grid', showindex=False)
    lebarTerminal = shutil.get_terminal_size().columns
    samping = (lebarTerminal - len(tabel.splitlines()[0])) // 2
    for line in tabel.splitlines():
        print(" " * samping + line)


# 2. Membuat data baru role Owner
def tambahProduk():
    df = loadData()
    lihatProduk()

    nama = inputTengah("Masukkan nama barang: ")
    hargaBeli = float(inputTengah("Masukkan harga barang: "))
    stok = int(inputTengah("Masukkan stok barang: "))
    hargaJual = float(inputTengah("Masukkan harga pokok barang: "))
    
    dataBaru = {'Nama': [nama], 'Harga Beli': [hargaBeli], 'Stok': [stok], 'Harga Jual': [hargaJual]}
    dfBaru = pd.DataFrame(dataBaru)
    
    df = pd.concat([df, dfBaru], ignore_index=True)
    
    simpanDataProduk(df)
    clear()
    print_tengah("Data berhasil ditambahkan.\n")
    lihatProduk()

# 3. Memperbarui data untuk role Owner
def updateProduk():
    df = loadData()
    lihatProduk()
    try:
        indexNo = int(inputTengah("Masukkan index barang yang ingin diupdate: "))
        trueindex = indexNo - 1
        if 0 <= trueindex < len(df):
            hargaBeliBaru = float(inputTengah("Masukkan harga beli baru: "))
            stok_baru = int(inputTengah("Masukkan stok baru: "))
            hargaJualBaru = float(inputTengah("Masukkan harga jual baru: "))
            
            df.at[trueindex, 'Harga Beli'] = hargaBeliBaru
            df.at[trueindex, 'Stok'] = stok_baru
            df.at[trueindex, 'Harga Jual'] = hargaJualBaru
        
            df.to_excel('produkk.xlsx', index=False)
            
            inputTengah("Produk berhasil diubah! Tekan Enter untuk melanjutkan...")
            clear()
            lihatProduk()
            print_tengah("Data berhasil diupdate.\n")
        else:
            print_tengah("Index tidak valid.\n")
    except ValueError as e:
        clear()
        print_tengah(f"Input tidak valid: {e}\n")
    except Exception as e:
        clear()
        print_tengah(f"Terjadi kesalahan: {e}\n")

# 4. Menghapus data untuk role Owner
def hapusProduk():
    df = loadData()
    lihatProduk()
    try:
        indexNo = int(inputTengah("Masukkan indeks barang yang ingin dihapus: "))
        trueindex = indexNo - 1
        if 0 <= trueindex < len(df):
            df.drop(index=trueindex, inplace=True)
            simpanDataProduk(df)
            print_tengah("Data berhasil dihapus.\n")
        else:
            print_tengah("Indeks tidak valid.\n")
    except ValueError:
        clear()
        print("Input tidak valid. Harus berupa angka.\n")
    except Exception as e:
        clear()
        print(f"Terjadi kesalahan: {e}\n")


# 5. Menghitung Profit Bersih untuk role Owner
def hitungProfit():
    df = pd.read_excel('produkk.xlsx')
    
    df['Profit'] = (df['Harga Jual'] - df['Harga Beli']) * df['Stok']

    totalProfit = df['Profit'].sum()
    simpanDataProduk(df)

    lihatProduk()
    
    print_tengah("-"*101)
    print_tengah(f"Total Profit: Rp {totalProfit:,}")
    print_tengah("-"*101)

#6. Pembelian untuk role Pembeli
def pembelian(username):
    data = bacaUser()
    akun = next((a for a in data['akun'] if a['username'] == username), None)
    if akun is None:
        print("Akun tidak ditemukan.")
        return
    
    df_produk = pd.read_excel('produkk.xlsx')  
    lihatProdukPembeli(username)

    try:
        no_produk = int(inputTengah("Masukkan nomor produk yang ingin dibeli: "))
        produk_index = df_produk[df_produk['No'] == no_produk].index[0]
        produk = df_produk.loc[produk_index]
    except (IndexError, ValueError):
        print_tengah("Nomor produk tidak valid.")
        return

    if produk['Stok'] <= 0:
        print_tengah("Stok produk habis.")
        return
    
    harga = produk['Harga Jual']
    if akun['saldo'] < harga:
        print_tengah("Saldo tidak mencukupi.")
        return

    akun['saldo'] -= harga

    df_produk.at[produk_index, 'Stok'] -= 1

    transaksi = {
        "ID": len(akun['riwayatPembelian']) + 1,
        "TANGGAL": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "PRODUK": produk['Nama'],
        "HARGA": f"{harga}" 
    }
    akun['riwayatPembelian'].append(transaksi)

    simpanUserData(data)
    df_produk.to_excel('produkk.xlsx', index=False)
    clear()
    loading()
    print_tengah(f"Pembelian berhasil! Saldo tersisa: Rp {akun['saldo']}")
    time.sleep(2)
    print_tengah(f"Stok {produk['Nama']} tersisa: {df_produk.at[produk_index, 'Stok']}")
    time.sleep(2)
    print_tengah("Riwayat pembelian diperbarui.")

# 7. Tampilkan riwayat pembelian untuk role pembeli
def tampilkanRiwayat(username):
    data = bacaUser()
    akun = next((a for a in data['akun'] if a['username'] == username), None)

    if akun is None or not akun['riwayatPembelian']:
        print_tengah("Riwayat pembelian tidak ditemukan.")
        return

    dfRiwayat = pd.DataFrame(akun['riwayatPembelian'])
    tabel= tabulate(dfRiwayat, headers='keys', tablefmt='fancy_grid', showindex=False)
    lebarTerminal = shutil.get_terminal_size().columns
    samping = (lebarTerminal - len(tabel.splitlines()[0])) // 2
    for line in tabel.splitlines():
        print(" " * samping + line)

# 8. Topup saldo untuk role pembeli
def topupSaldo(username, jumlah, file_path='datausername.json'):
    data = bacaUser()

    for akun in data['akun']:
        if akun['username'] == username:
            if 'saldo' not in akun:
                akun['saldo'] = 0
            
            akun['saldo'] += jumlah
            
            simpanUserData(data, file_path)

            print_tengah(f"Saldo berhasil ditambah sebesar Rp {jumlah}. Saldo saat ini: Rp {akun['saldo']}\n")
            return

 # 9. Lihat saldo untuk role pembeli   
def lihatSaldo(username):
    data = bacaUser()
    for akun in data['akun']:
        if akun['username'] == username and 'saldo' in akun:
            print_tengah(f"Saldo {akun['username']} sebesar Rp {akun['saldo']}.\n")
            return akun['saldo']
    print_tengah("Username tidak ditemukan atau saldo belum diatur.\n")
    return None


