#Diketahui sebuah list memiliki nilai-nilai elemen sebagai berikut:
#[7, 1, 14, 21, 28, 42, 35]
#1. Urutkan list di atas menggunakan algoritma Bubble Sort
#2. Carilah nilai “21” menggunakan algoritma pencarian sequensial

nilai_list = [7,1,14,21,28,42,35]

#1
for i in range(len(nilai_list)-1,0,-1):
    for j in range(i):
        if nilai_list[j]>nilai_list[j+1]:
            urut = nilai_list[j]
            nilai_list[j]=nilai_list[j+1]
            nilai_list[j+1]=urut
print(nilai_list)

#2. 
cari = 21
nilai_list = [7,1,14,21,28,42,35]
indeks = 0
iterasi = 0
akhir = len(nilai_list)-1
found = False
while indeks <= akhir and not found:
    iterasi += 1
    if nilai_list[indeks] == cari:
        found = True
    else:
        indeks = indeks + 1
if found:
    print("angka yang dicari terletak pada indeks: ", indeks)
    print("Itersi sebanyak = ", iterasi, "kali")
else:
    print("angka yang dicari tidak ditemukan!")
    print("Iterasi dilakukan sebanyak =", iterasi, "kali")
