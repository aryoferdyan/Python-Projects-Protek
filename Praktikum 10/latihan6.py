import os, sys
from os.path import split
from typing import Text
file = open(os.path.join(sys.path[0], "6.txt"), "r")
fil2 = open(os.path.join(sys.path[0], "6_output.txt"), "w+")

src = (file.read()).split(',')

txt = str(src[0])
n   = int(src[1])
ecr = ''

for i in txt:
    if i.isupper():
        awl = ord(i) - ord('A')
        akh = (awl + n) % 26
        ak2 = akh + ord('A')
        ecr = ecr + chr(ak2)
    else:
        ecr += i

fil2.write(ecr)