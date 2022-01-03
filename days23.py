from typing import List


List = []

while True :
    angka = int(input("Masukkan angka : "))
    List.append(angka)
    stop = input('Apakah angka sudah cukup? (y/t) : ')
    if stop == 'y' :
        print('Angka yang anda masukkan : ', len(List))
        print('Total List :', List)
        break
print('Angka sebelum diurutkan :', List)
List.sort()
print('Angka yang sudah diurutkan : ', List)
