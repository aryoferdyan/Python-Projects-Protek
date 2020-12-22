import os, sys, time
file = open(os.path.join(sys.path[0], "latihan2_output.txt"), "r")

print('\nMasukkan NIM yang mau dicari : ',end='')
nim = input()

lsb = {}
fnd = 0
for i in file.readlines():
    lst = i.split('|')
    lsb.update({'nim': lst[0]})
    lsb.update({'nma': lst[1]})
    lsb.update({'alm': lst[2]})
        
    
    if nim in lsb.values():
        time.sleep(1)
        print('\nData Mahasiswa')
        print('NIM'.ljust(8),': ',lsb.get('nim', 0))
        print('Nama'.ljust(8),': ',lsb.get('nma', 0))
        print('Alamat'.ljust(8),': ',lsb.get('alm', 0))
        fnd = 1

if fnd == 0:
    time.sleep(1)
    print('\nData mahasiswa tidak ditemukan\n')
    time.sleep(1)
