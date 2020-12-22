import os, sys
file = open(os.path.join(sys.path[0], "latihan2_output.txt"), "r")

lsb = {}
dataMhs = []

for i in file.readlines():
    lst = i.split('|')
    lsb.update({'nim': lst[0]})
    lsb.update({'nma': lst[1]})
    lsb.update({'alm': lst[2]})
    #dataMhs.update({'',lsb})
    print(lsb)
    dataMhs.append(lsb)

print(dataMhs)

