import os, sys, time, datetime

def diffDate(x): 
    now = datetime.datetime.now()
    nx = x.split('-')

    # (thn, tgl, bln) 
    a = datetime.datetime(now.year, now.month, now.day) 
    b = datetime.datetime(int(nx[0]), int(nx[1]), int(nx[2])) 
     
    selisih = a-b  
    
    return selisih.days

file = open(os.path.join(sys.path[0], "Project_1_output.txt"), "r")

print('')
cari = input('Masukkan Kode Member\t: ')
print('')

#status file ditemukan/tidak
sts = False

for i in file.readlines():
    x = i.split('|')

    if x[0] == cari:
        time.sleep(1)
        sts = True
        ter = diffDate(x[4])
        if ter < 0:
            ter = 0
        den = 2000 * ter
        now = datetime.datetime.today()
        tg2 = '-'.join([str(now.year), str(now.month), str(now.day)]) 
        
        print('Data Peminjaman Buku')
        print('Kode Member\t\t:',x[0])
        print('Nama Member\t\t:',x[1])
        print('Judul Buku\t\t:',x[2])
        print('Tanggal Mulai Peminjaman:',x[3])
        print('Tanggal Maks Peminjaman\t:',x[4])
        print('Tanggal Pengembalian\t:',tg2)
        print('Terlambat\t\t:',ter,'hari')
        print('Denda\t\t\t: Rp',den)
        print('')

if sts == False:
    time.sleep(1)
    print('Kode tidak ditemukan/tidak terdaftar\n')
