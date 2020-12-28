from datetime import *
import os, sys
file = open(os.path.join(sys.path[0], "Project_1_output.txt"), "a")

print('')

n = 'y'
while n == 'y' or n == 'Y':
    kode = input('Masukkan Kode Member\t: ')
    nama = input('Masukkan Nama Member\t: ')
    judl = input('Masukkan Judul Buku\t: ')
    tgl1 = datetime.date(datetime.now())
    tgl2 = tgl1 + timedelta(days=7)

    hasl = '|'.join([kode,nama,judl,str(tgl1),str(tgl2)])
    print(hasl)
    file.write(hasl)
    file.write('\n')

    print('')
    n = input('Ulangi lagi (y/n) :')
    print('')


