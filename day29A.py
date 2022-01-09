#Menambahkan elemen
angka = [1,2,3,4,5]
angka.extend([9,10,11])
print(angka)

#menghapus
del angka[0]
print(angka)

#menghapus menggunakan nama/angka element
angka.remove(11)
print(angka)

#menghapus
angka.pop(3)
print(angka)

#menambahkan elemen
angka.extend([10,99,70,21,33,45])
print(angka)

#mengurutkan elemen
angka.sort()
print(angka)

angka.reverse()
print(angka)