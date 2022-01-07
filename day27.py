#Mencari nilai
nilai = [1,7,43,23,45,67,10,19]
cari = int(input('Masukkan nilai yang ingin dicari : '))
index = -1

for i in range(len(nilai)) :
    if nilai[i] == cari :
        index = i
        break
if index == -1 :
    print('Maaf nilai yang anda cari tidak ada!')
else :
    print('angka', cari,'yang anda cari berada pada indeks :', index)
