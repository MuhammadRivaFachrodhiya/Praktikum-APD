import os
clear = lambda: os.system('cls || clear')
clear()

data_mhs = [
    {
     "nama" : "ucup",
     "role" : "admin"
     },

    {
     "nama" : "michael",
     "role" : "user"
    }
]

print(data_mhs[0]['nama'])
print(data_mhs[1]['role'])

# print(data_mhs["dosen"]["Nama"])
# print(len(data_mhs))
# del data_mhs["nim"]

# cache = data_mhs.pop("nim")
# print(data_mhs)
# print(cache)
# data_mhs["id"] = cache
# print(data_mhs)

# print(data_mhs.clear())

# data_mhs['alamat'] = "Samarinda"
# data_mhs['alamat'] = "Tenggarong"

# data_mhs.update({"alamat" :"Samarinda"})
# data_mhs.update({"alamat" :"Tenggarong"})

# print(data_mhs.get('mapel','Tidak ada'))

# for data in data_mhs:
#     print(data)

# for key_data, value_data in data_mhs.items():
#     print(f"Key : {key_data}\nValue : {value_data}\n")

# print(data_mhs['nama'])
# print(data_mhs['nim'])

# key = "apel", "jeruk", "mangga"
# value = 1
# buah = dict.fromkeys(key, value)
# print(buah)

# for key in data_mhs:
    # print(data_mhs[key])

# Nilai = {
#     "Matematika" : 80,
#     "B. Indonesia" : 90,
#     "B. Inggris" : 81,
#     "Kimia" : 20
# }
# #sebelum Setdefault
# print(Nilai)
# print("")
# #menggunakan setdefault
# print("Nilai : ", Nilai.setdefault("Kimia", 70))
# print("")
# #setelah menggunakan setdefault
# print(Nilai)