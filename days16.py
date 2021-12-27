matriks = [[2,3,4],
        [5,6,8],
        [1,2,1],
        [9,8,7]]

#Menampilkan elemen-elemen kolom pertama
list = []
for i in matriks:
    list.append(i[0])
print(list)


print('---------------------------------')

# Menngganti element
matriks[1][2] = 10
for i in matriks:
    print(i)