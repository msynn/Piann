angkaAwal = int(input('Masukkan angka awal : '))
angkaAkhir = int(input('Masukkan angka akhir : '))
x = []
y = []
for i in range(angkaAwal,angkaAkhir+1):
    if i%2 == 0:
        x.append(i)
    if i%2 == 1:
        y.append(i)
    
print('Angka genap : ', x)
print('Angka ganjil : ', y)



angka = int(input('Masukkan angka : '))
if angka %2 == 0:
    print('Angka',angka,'adalah bilangan genap')
elif angka %2 == 1:
    print('Angka', angka, 'adalah bilangan ganjil')