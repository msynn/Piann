#list bilangan prima dan menjumlah total
prima = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
for i in prima:
    print(i)

prima = sum(prima)
print("Jumlah keseluruhan bilangan prima adalah =",prima)

#membuat list memakai perulangan
list = []
for i in range(10,100,10):
    list.append(i)
print(list)

#menghapus element
list.pop(2)
print(list)

#menambahkan element
list.insert(2,25)
print(list)

#list Pulau
pulau = ["Sulawesi","Jawa","Kalimantan","Sumatera","Papua","Nusa tenggara barat","Maluku"]
print(pulau)

#menampilkan elemen ke 2 dan 3
print(pulau[1:3])

#menampilkan elemen kedua dari belakang
print(pulau[-2])

#menghapus elemen ke 2
pulau.pop(2)
print(pulau)

#menggabung himpunan
a = {1,2,3,4,5,6}
b = {3,4,5,6,7,8}
print(a.union(b))


#contoh list
odd = [1,3,5,7,9]
print(odd[:3]) #or
print(odd[0])
print(odd[1])
print(odd[2])
