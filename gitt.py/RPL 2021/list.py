#menampung perulangan ke list
print("=======================")
bilangan = []
for i in range(10,100,10):
    bilangan.append(i)
print(bilangan)

#menghapus elemen ke 3
print("=======================")
bilangan.pop(2)
print(bilangan)

#Menampilkan elemen ke 5
print("=======================")
print(bilangan[4])

#menambahkan nilai '25' ke elemen ketiga dalam list
print("=======================")
bilangan.insert(2,25)
print(bilangan)

