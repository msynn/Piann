def volume_kubus():
    print("MENGHITUNG VOLUME KUBUS")
    print("-"*30,'\n')
    panjang_rusuk = int(input('Masukkan panjang persegi (cm) : '))
    hasil = panjang_rusuk ** 3
    print("Volume dari kubus yang memiliki panjang rusuk {} adalah : {}" .format(panjang_rusuk,hasil))
    return hasil

def volume_balok():
    print("MENGHITUNG VOLUME BALOK")
    print("-"*30,'\n')
    P = int(input("Masukkan panjang (cm) : "))
    L = int(input("Masukkan Lebar (cm) : "))
    T =  int(input("Masukkan tinggi (cm) : "))
    hasil = P*L*T
    print("Volume dari balok yang memiliki panjang {}, luas {}, tinggi {}, adalah : {} cm" .format(P,L,T,hasil))
    return hasil

print('-'*30)
print("PROGRAM MENGHITUNG VOLUME")
print('-'*30)
end = "y"
while end == "y" :
    print("1. Volume Kubus")
    print("2. Volume balok")
    pilihan = int(input("Masukkan Kode : "))
    if pilihan == 1 : 
        volume_kubus()
    elif pilihan == 2 :
        volume_balok()
    else :
        print("Invalid kode!")

    end = input("Lanjut ? y/n : ")

