import os, sys
file = open(os.path.join(sys.path[0], "5.txt"), "r")
fail = open(os.path.join(sys.path[0], "5_output.txt"), "w+")

lst = []
for i in file.readlines():
    lst = i.split('|')
    hsl = int(lst[0]) + int(lst[1])
    fail.write(str(hsl))
    fail.write('\n')