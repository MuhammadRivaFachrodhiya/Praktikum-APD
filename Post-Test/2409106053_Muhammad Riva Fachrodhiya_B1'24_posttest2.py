#ini input
nama = input("Nama Anda Siapa ")
umur = int(input("Umur Anda Berapa "))
alamat = input("Alamat Anda Dimana ")
berat_badan = float(input("Berat Badan Anda Berapa (dalam satuan kg)   "))
tinggi_badan = float(input("Tinggi Badan Anda Berapa (dalam satuan cm) "))
pekerjaan = input("Pekerjaan Anda Apa   ")
verifikasi_data = input("Apakah Data Anda Sudah Benar? (True/False)    ")
jumlah_numerik = umur + berat_badan + tinggi_badan

#ini output
print("=" * 35)
print("          Bio Data Anda           ")
print("=" * 35)
print(f"Nama                 : {nama}")
print(f"Umur                 : {umur} Tahun")
print(f"Alamat               : {alamat}")
print(f"Berat Badan          : {berat_badan} kg")
print(f"Tinggi Badan         : {tinggi_badan} cm")
print(f"Pekerjaan            : {pekerjaan}")
print(f"Cek Data Anda        : {'Sudah' if verifikasi_data == 'True' else 'False'}")
print("=" * 35)

#jumlah numerik
print(f"Jumlah Numerik       : {jumlah_numerik}")
print("=" * 35)

