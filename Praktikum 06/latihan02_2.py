
def starFormation(n):
    i = 0
    while (i < n):
        j = i
        while (j < n):
            print('* ', end='')
            j += 1
        print()
        i += 1

starFormation(5)