import datetime

mahasiswa1 = {
     'nama':'Ucup surucup',
     'nim':'1902201',
     'sks':144,
     'beasiswa':True,
     'lahir':datetime.datetime(2000,4,5)
}
mahasiswa2 = {
     'nama':'Otong surotong',
     'nim':'1902202',
     'sks':143,
     'beasiswa':False,
     'lahir':datetime.datetime(2000,7,9)
}
mahasiswa3 = {
     'nama':'Asep si kasyep',
     'nim':'1902203',
     'sks':142,
     'beasiswa':False,
     'lahir':datetime.datetime(2000,9,2)
}

data_mahasiswa = {
     'MAH001':mahasiswa1,
     'MAH002':mahasiswa2,
     'MAH003':mahasiswa3
}

print(f"{'KEY':<6} {'NAMA':<16} {'SKS':<3} {'BEASISWA':^9} {'LAHIR':<10}")
print("_"*50)

for mahasiswa in data_mahasiswa:
     
    key = mahasiswa
    nama = data_mahasiswa[key]['nama']
    sks = data_mahasiswa[key]['sks']
    beasiswa = data_mahasiswa[key]['beasiswa']
    lahir = data_mahasiswa[key]['lahir'].strftime("%x")
    
    print(f"{key:<6} {nama:<16} {sks:<3} {beasiswa:^9} {lahir:<10}")