import os, sys
file = open(os.path.join(sys.path[0], "6_output.txt"), "r")
fil2 = open(os.path.join(sys.path[0], "7_output.txt"), "w+")

try:
    print('\nMasukkan nilai n = ',end='')
    n   = int(input())
    txt = str(file.read())
    scr = ''

    for i in txt:

        if i.isupper():
            awl = ord(i) - ord('A')
            akh = (awl - n) % 26
            ak2 = akh + ord('A')
            scr = scr + chr(ak2)
        else:
            scr += i

    fil2.write(scr)

except ValueError:
    print('\nn harus integer\n')

    