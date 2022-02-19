angka =int(input("masukkan angka : "))
def satuan():
    print('''1. milimeter
    2. centimeter
    3. desimeter
    4. meter
    5. dekameter
    6. hektometer
    7. kilometer''')
satuan()
a = int(input("masukkan satuan awal : (masukkan dalam angka)  "))
satuan()
b = int(input("masukkan satuan konversi : (masukkan dalam angka) "))
jarak = a - b
x = 10 ** jarak
hasil = angka * x
print(hasil)