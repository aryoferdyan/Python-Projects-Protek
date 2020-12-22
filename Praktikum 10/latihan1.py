import os, sys

try:
    #file = open("D:/UNS/Github/Python Projects/Praktikum 10/1.txt",'r')
    
    #input direktori sama dengan folder kode
    file = open(os.path.join(sys.path[0], "1.txt"), "r")

    gjl = 0
    gnp = 0

    for i in file.readlines():
        x = int(i)
        if x == 0:
            continue
        if x % 2 == 0:
            gnp += 1
        if x % 2 == 1:
            gjl += 1

    print("Banyaknya bilangan genap  :",gnp)
    print("Banyaknya bilangan ganjil :",gjl)

except FileNotFoundError:

    print('\n File tidak ditemukan coba direktori lain \n')
