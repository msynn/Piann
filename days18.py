total = 0
barang = []
harga = []

while True:
    print('''Daftar Barang\n
    1. Roti\t\t 5000
    2. Minuman dingin\t 1000
    3. Keripik\t\t 2000
    4. Pensil\t\t 4000
    5. Buku Tulis kecil\t 3000
    6. Buku Tulis Besar\t 5000
    7. Pulpen\t\t 4000
    8. Spidol\t\t 5000
    9. Baterai\t\t 2500
    10. penghapus\t 3000''')

    kode =  int(input("Masukkan kode barang : "))
    if kode == 1:
        barang.append('roti')
        harga.append(5000)
        total += 5000
    elif kode == 2:
        barang.append('Minuman Dingin')
        harga.append(1000)
        total += 1000
    elif kode == 3:
        barang.append('Keripik')
        harga.append(2000)
        total += 2000
    elif kode == 4:
        barang.append('Pensil')
        harga.append(4000)
        total += 4000
    elif kode == 5:
        barang.append('Buku Tulis Kecil')
        harga.append(3000)
        total += 3000
    elif kode == 6:
        barang.append('Buku Tulis Besar')
        harga.append(5000)
        total += 5000
    elif kode == 7:
        barang.append('Pulpen')
        harga.append(4000)
        total += 4000
    elif kode == 8:
        barang.append('Spidol')
        harga.append(5000)
        total += 5000
    elif kode == 9:
        barang.append('Baterai')
        harga.append(2500)
        total += 2500
    elif kode == 10:
        barang.append('Penghapus')
        harga.append(3000)
        total += 3000
    else:
        print('Kode Tidak Valid!!!')
    
    lanjut = input('Lanjut belanja (ya/tidak) : ')
    if lanjut == 'tidak':
        print("")
        break

print('Barang yang dibeli : ', barang)
print('Harga barang : ', harga)
print("total yang harus dibayar :", total)

bayar = int(input('Masukkan uang Pembayaran : '))
if bayar > total :
    jadi = bayar - total
    print('Terimakasih Transaksi anda berhasil!')
    print('Kembalian anda : ', jadi)
elif bayar < total :
    jadi =  bayar - total
    print('Uang anda Kurang : ', jadi)
else:
    print('Terimakasih Telah Belanja di toko kami')

        


