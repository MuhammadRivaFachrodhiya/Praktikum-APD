import pandas as pd
from tabulate import tabulate
import os 
def clear():
    os.system('cls||clear')

# Membaca data dari file Excel
def load_data():
    try:
        df = pd.read_excel('produkk.xlsx')
        return df
    except FileNotFoundError:
        print("File tidak ditemukan. Pastikan file 'produkk.xlsx' tersedia.")
        return pd.DataFrame(columns=['No', 'Nama', 'Harga Beli', 'Stok', 'Harga Jual'])

# Menyimpan data ke file Excel dengan mengisi ulang kolom "No"
def save_data(df):
    df.reset_index(drop=True, inplace=True)  # Reset indeks untuk menghindari duplikasi
    df['No'] = df.index + 1  # Isi kolom "No" sesuai indeks (mulai dari 1)
    # Menata ulang kolom agar "No" berada di paling kiri
    df = df[['No', 'Nama', 'Harga Beli', 'Stok', 'Harga Jual']]
    df.to_excel('produkk.xlsx', index=False)

# 1. Create (Membuat Data Baru)
def add_product():
    df = load_data()
    nama = input("Masukkan nama barang: ")
    hargaBeli = float(input("Masukkan harga barang: "))
    stok = int(input("Masukkan stok barang: "))
    hargaJual = float(input("Masukkan harga pokok barang: "))
    
    # Data baru yang ingin ditambahkan
    data_baru = {'Nama': [nama], 'Harga Beli': [hargaBeli], 'Stok': [stok], 'Harga Jual': [hargaJual]}
    df_baru = pd.DataFrame(data_baru)
    
    # Menggabungkan data baru dengan data yang sudah ada
    df = pd.concat([df, df_baru], ignore_index=True)
    
    # Memperbarui dan menyimpan data
    save_data(df)
    print("Data berhasil ditambahkan.\n")

# 2. Read (Membaca Data)
def read_products():
    df = load_data()
    # Menggunakan tabulate untuk tampilan yang rapi
    print(tabulate(df, headers='keys', tablefmt='fancy_grid', showindex=False))

# 3. Update (Memperbarui Data)
def update_product():
    df = load_data()
    nama = input("Masukkan nama barang yang ingin diupdate: ")
    if nama in df['Nama'].values:
        hargaBeliBaru = float(input("Masukkan harga beli baru: "))
        stok_baru = int(input("Masukkan stok baru: "))
        hargaJualBaru = float(input("Masukkan harga jual baru: "))
        
        df.loc[df['Nama'] == nama, 'Harga'] = hargaBeliBaru
        df.loc[df['Nama'] == nama, 'Stok'] = stok_baru
        df.loc[df['Nama'] == nama, 'Harga Pokok'] = hargaJualBaru
        save_data(df)
        print("Data berhasil diupdate.\n")
    else:
        print("Produk tidak ditemukan.\n")

# 4. Delete (Menghapus Data)
def delete_product():
    df = load_data()
    nama = input("Masukkan nama barang yang ingin dihapus: ")
    df = df[df['Nama'] != nama]
    save_data(df)
    print("Data berhasil dihapus.\n")

# Menghitung Profit Bersih
def calculate_profit():
    # Membaca file Excel
    df = pd.read_excel('produkk.xlsx')
    
    # Membersihkan kolom Harga Beli dan Harga Jual
    df['Harga Beli'] = df['Harga Beli'].replace('[Rp. ]', '', regex=True).str.replace('.', '').astype(int)
    df['Harga Jual'] = df['Harga Jual'].replace('[Rp. ]', '', regex=True).str.replace('.', '').astype(int)
    
    # Menghitung profit
    df['Profit'] = (df['Harga Jual'] - df['Harga Beli']) * df['Stok']

    # Menghitung total profit
    total_profit = df['Profit'].sum()

     # Menampilkan data dengan profit
    print(tabulate(df, headers='keys', tablefmt='fancy_grid', showindex=False))
    print("-"*101)
    print(f"\t\t\t\t   Total Profit: Rp {total_profit:,}")
    print("-"*101)
# Memanggil fungsi calculate_profit
calculate_profit()


# Menu CRUD
def menu():
    while True:
        clear()
        print("Menu CRUD:")
        print("1. Tambah Produk")
        print("2. Tampilkan Produk")
        print("3. Update Produk")
        print("4. Hapus Produk")
        print("5. Hitung Profit Bersih")
        print("6. Keluar")
        choice = input("Pilih menu (1-6): ")
        if choice == '1':
            clear()
            add_product()
        elif choice == '2':
            clear()
            read_products()
            input("Tekan Enter")
        elif choice == '3':
            update_product()
        elif choice == '4':
            delete_product()
        elif choice == '5':
            clear()
            calculate_profit()
            input("\nTekan Enter. . . .")
        elif choice == '6':
            print("Keluar dari program.")
            break
        else:
            print("Pilihan tidak valid.\n")

# Memulai program
menu()
