data_dict = {
"uc" : 'ucup',
'og' : 'otong',
'dd' : 'dudung'
}
print(data_dict)

lendict = len(data_dict)
panjang = lendict

print(f"Panjang dari data dict = {panjang}")

#mengecek data
dict = "sup" in data_dict
print(dict)

#atau

key = "cup"
check = key in data_dict
print(f"Apakah {key} ada di data_dict? = {check}")

key = "uc"
check = key in data_dict
print(f"Apakah {key} ada di data_dict? = {check}")

#mengambil data dictionary

data = data_dict['uc'] # kalau tidak terdeteksi maka akan menampilkan pesan error sebagaimana biasanya
print(f"Data diambil 1 = {data}")
#tidak dengan menggunakan .get()
data = data_dict.get('uc')
print(f"Data diambil = {data}")


data = data_dict.get('c', 'kaga ketemu') #kalau tidak terdeteksi ada di dictionary maka akan output "none" kecuali dikasih custom message setelah koma untuk mengganti kata none itu
print(f"Data diambil = {data}")

#mengupdate dictionary
#mengubah value
data_dict['og'] =  "otong markotong"
print(f" Data skrng = {data_dict}")

#menggunakan .update()

data_dict.update({'dd' : 'dadang tededeng'}) #bila terdeteksi ada key yg sesuai maka akan mengubah yg ada/overwrite
print(data_dict)
#dan jika tidak ada yg sama antara key di dalam kurung .update() dengan key yg ada di dictionary maka akan menambahkan data baru
data_dict.update({'uj' : 'ujang sanjang'})
print(data_dict) #2 IN 1 feature

#menghapus data

del data_dict['uj']
print(data_dict)

#del data_dict['up']
#print(data_dict)     ← output error karena tidak ada key di dictionary yg sesuai target

#====================

teman_teman = {
    "cup":"ucup surucup",
    "tong":"otong markotong",
    "dung":"dudung mardudung",
    "sep":"asep markesep",
    "jang":"ujang markujang"
}

print("\nKeys\n")
keys = teman_teman.keys()
print(keys)

for key in teman_teman.keys():
    print(f"Key-nya adalah = {key}")


print("\nValues\n")
value = teman_teman.values()
print(value)

for va in teman_teman.values():
    print(f"Value-nya adalah {va}")
    
print("\nItems\n")
item = teman_teman.items()
print(item)

for it in teman_teman.items():
    print(f"Item-nya adalah {it}")
    
print("\n\nGABUNGAN\n\n")

for key,va in teman_teman.items():
    print(24*"=" + "\n" + key + " " + "===" + " " + va)
    
#======================

teman_teman = {
    "cup":"ucup surucup",
    "tong":"otong markotong",
    "dung":"dudung mardudung",
    "sep":"asep markesep",
    "jang":"ujang markujang"
}

friends = teman_teman.copy()
print("\n\n",teman_teman)
print("\n",friends)
print("\n\n===========CHANGE==========")
friends["tong"] = "otong sotong"
print("\n\n",teman_teman)
print("\n",friends)

#mirip seperti list ↓↓↓
#friends["cup"] = "supucup"
#print("\n\n",teman_teman)
#print("\n",friends)


#pop mengambil sesuai target key dan menampilkan value
print("\n\n" + "="*15 + "POP" + "="*15)
datadung = teman_teman.pop("dung")
print("data dudung = ",datadung)
print("\nData sisa : \n",teman_teman)
#popitem mengambil data terakhir dan menampilkan key dan value
print("\n\n"+"="*14+"POPITEM"+"="*14)
datajang = teman_teman.popitem()
print("data terakhir = ",datajang)
print("\nData sisa : \n",teman_teman)

#=========================







































































































