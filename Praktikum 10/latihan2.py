import os, sys
file = open(os.path.join(sys.path[0], "latihan2_output.txt"), "w+")

lgi = 'y'
while lgi == 'y' or lgi == 'Y':
    nim = input('Masukkan NIM\t\t: ')
    nma = input('Masukkan Nama Mhs\t: ')
    alm = input('Masukkan Alamat\t\t: ')

    x = '|'.join([nim,nma,alm])
    file.write(x)
    file.write('\n')
    
    print('')
    lgi = input('Ulangi input lagi (y/n)\t: ')
    print('')


