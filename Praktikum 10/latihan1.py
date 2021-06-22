jumlah = int(input('Jumlah'))
kat = int(input('Kategori'))

if kat == '1':
    harga = 255000
if kat == '2':
    harga = 150000
if kat == '3':
    harga = 75000

total = jumlah*harga
print(total)
