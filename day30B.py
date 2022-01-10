#Mengetahui bilangan ganjil/genap
angka = int(input('Masukkan angka : '))
if angka %2 == 0:
    print('Angka',angka,'adalah bilangan genap')
elif angka %2 == 1:
    print('Angka', angka, 'adalah bilangan ganjil')
