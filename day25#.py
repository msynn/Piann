#Algoritma Sequential Search

cari = int(input('Masukkan angka yang ingin dicari : '))
a = [1,2,3,4,5]
indeks = 0
iterasi = 0
akhir = len(a)-1
found = False
while indeks <= akhir and not found :
    iterasi += 1
    if a[indeks] == cari :
        found = True
    else :
        indeks = indeks + 1
if found:
    print('Angka yang dicari berada pada indeks ke : ', indeks)
    print('Iterasi sebanyak', iterasi, 'Kali')
else :
    print('Angka yang dicari tidak di temukan!')
    print('Iterasi dilakukkan sebanyak ', iterasi, 'Kali')
