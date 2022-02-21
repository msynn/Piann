barang = {"1":"Tas","2":"Kaos","3":"Sepatu"}
harga = {"1":10000,"2":20000,"3":30000}
print("Daftar Barang")
print("1. Tas Rp. 10.000")
print("2. Kaos Rp. 20.000")
print("3. Sepatu Rp. 30.000")
print("Pilih Barang")
total = 0

while True :
    pilihan = int(input("Masukkan Pilihan : "))
    if pilihan == 1 :
        total += harga["1"]
        print("Anda Memilih",barang["1"])
        print("Harga",barang["1"],"Rp.",harga["1"])
    elif pilihan == 2 :
        total += harga["2"]
        print("Anda Memilih",barang["2"])
        print("Harga",barang["2"],"Rp.",harga["2"])
    elif pilihan == 3 :
        total += harga["3"]
        print("Anda Memilih",barang["3"])
        print("Harga",barang["3"],"Rp.",harga["3"])
    elif pilihan not in barang :
        print("Pilihan tidak ada")


    lanjut = input("Lanjutkan (y/n) : ")
    if lanjut == "t" :
        break
    

print("Total bayar : ",total)
bayar = int(input("bayar : "))
kembalian = bayar - total
print("Kembalian : ",kembalian)
print("Terima Kasih Telah Berbelanja")
