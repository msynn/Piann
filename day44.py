print("=============>MEMBUAT SEGITIGA<============\n")

angka = int(input("Masukka ukuran segitiga : "))

for i in range(1,angka+1):
    print((angka-i)*" " +(i * "*") + ((i-1) * "*"))