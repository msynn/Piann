print("============Program Tebak Angka==============\n")
angka = 10
#dificulty
print("Tingkat Kesulitan : ")
print("1. Hard")
print("2. Normal")
print("3. Easy")
dificulty = int(input("Masukkan Kode Tingkat Kesulitan : "))
if dificulty == 1 :
    tingkatKesulitan = 2
elif dificulty == 2 :
    tingkatKesulitan = 5
elif dificulty == 3 :
    tingkatKesulitan = 10

for i in range (tingkatKesulitan) :
    tebakan = int(input('Masukkan Angka : '))
    if tebakan > angka :
        print("Angka Terlalu Besar!")
    elif tebakan < angka :
        print("Angka Terlalu Kecil!")
    else :
        print("Selamat, Tebakanmu benar!")
        break
else :
    print("\n ----------GAME OVER----------")
