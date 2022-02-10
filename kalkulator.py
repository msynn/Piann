a = int(input("Masukkan angka : "))
pilihan = input("Pilih operasi (+, -, *, /) : ")
b = int(input("Masukkan angka : "))
angka = []
if pilihan == '+':
    hasil = a + b
    angka.append(hasil)
elif pilihan == '-':
    hasil = a - b
    angka.append(hasil)
elif pilihan == '*':
    hasil = a * b
    angka.append(hasil)
elif pilihan == '/':
    hasil = a / b
    angka.append(hasil)
while True :
    pilihan2 = input("Pilih operasi (+, -, *, /,=) : ")
    if pilihan2 == '=':
        print(hasil)
        break
    c = int(input("Masukkan angka :"))
    if pilihan2 == '+':
        hasil = hasil + c
        angka.append(hasil)
    elif pilihan2 == '-':
        hasil = hasil - c
        angka.append(hasil)
    elif pilihan2 == '*':
        hasil = hasil * c
        angka.append(hasil)
    elif pilihan2 == '/':
        hasil = hasil / c
        angka.append(hasil)
