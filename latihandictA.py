import datetime
import os
import string
import random

red = '\033[91m'
green = '\033[92m'
blue = '\033[94m'
bold = '\033[1m'
bg = '\033[3m'
underline = '\033[4m'
end = '\033[0m'

grs = f"{red}{bold}|{end}"
#TEMPLATE MAHASISWA
os.system("clear")

mahasiswa_template = {
     'nama':'nama',
     'nim':'00000000',
     'sks_lulus':0,
     'lahir':datetime.datetime(1111,1,11)
}

#dict kosong

data_mahasiswa = {}
#================

while True:
     
     print("\n\n\n"+bold+blue+"—"*65+end)
     print(f"\n\n{bold}{'SELAMAT DATANG':^65}")
     print(f"{'DI':^65}")
     print(f"{'DATA MAHASISWA':^65}{end}\n\n")
     print(bold+blue+"—"*65+end+"\n\n")
     print(bold+"MASUKAN DATA MAHASISWA"+end)
     mahasiswa = dict.     fromkeys(mahasiswa_template.keys())
     
     mahasiswa['nama'] = input(bold+"NAMA\t\t  : ")
     mahasiswa['nim'] = int(input("NIM\t\t  : "))
     mahasiswa['sks_lulus'] = int(input("SKS LULUS\t  : "))
     tahun = int(input("TAHUN LAHIR (YYYY): "))
     bulan = int(input("BULAN LAHIR (1-12): "))
     tanggal = int(input("TANGGAL LAHIR 1-31: "+end))
     mahasiswa['lahir'] = datetime.datetime(tahun,bulan,tanggal)

     key = ''.join((random.choice(string.ascii_uppercase) for i in range(7)))
     
     data_mahasiswa.update({key:mahasiswa})
     
     print(f"\n{bold}{'—'*64}{end}\n{underline}{bold}{green}{' KEY':^7}{end}{grs}{underline}{bold}{green}{'NAMA':^41}{end}{grs}{underline}{bold}{green}{'SKS':<3}{end}{grs}{underline}{bold}{green}{'LAHIR':^10}{end}")
     
     
     for mahasiswa in data_mahasiswa:
          
          key = mahasiswa
          nama = data_mahasiswa[key]['nama']
          sks = data_mahasiswa[key]['sks_lulus']
          lahir = data_mahasiswa[key]['lahir'].strftime("%x")
          
          print(f"{underline}{bold}{key:<7}{end}{grs}{end}{underline}{bold}{nama:^41}{end}{grs}{underline}{bold}{sks:<3}{end}{grs}{underline}{bold}{lahir:^10}{end}")
     
     islanjut = input(bold+"\n\nLanjut"+bg+"(y/n)"+end+bold+"? : "+end)
     
     if islanjut == "y":
          os.system("clear")
          continue
     elif islanjut == "n":
          break
     elif islanjut != "y" or "n":
          print(f"\n\n{bg}{bold}Tolong pilih salah satu\n{'(y/n)':^23}{end}")
          break
print(f"{bold}{green}\n\nAkhir dari program,\nTerimakasih{end}")