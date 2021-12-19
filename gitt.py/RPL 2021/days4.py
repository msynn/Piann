
print('='*5,"ATM SEDERHANA",'='*5)
pin = 123456
saldo = 100000000
nomor_Tujuan = 796501011612536
pin2 = int(input("Masukkan Pin :"))
if pin2 == pin:
    print("Selamat Datang FYAN RAMADHAN")
    print("PILIH OPTION :")
    pilihan = ['1. Tarik Tunai','2. Transfer','3. Cek Saldo']
    for i in pilihan :
        print(i)
    option = int(input("Pilih OPTION :"))
    if option == 1:
        jumlah_Tarik = int(input("Masukkan jumlah uang yang ingin anda tarik:"))
        if jumlah_Tarik <= saldo:
            print("Silahkan ambil uang anda")
            print("Sisa saldo anda =", saldo-jumlah_Tarik)
        else:
            print("maaf saldo anda tidak cukup")
    if option == 2:
        transferKe = int(input("Masukkan rekening tujuan :"))
        if transferKe == nomor_Tujuan:
            jumlah_Transfer = int(input("Masukkan Jumlah yang ingin di transfer :"))
            if jumlah_Transfer <= saldo:
                print("Transfer anda sukses, sebesar :", jumlah_Transfer, "Ke Rekening", nomor_Tujuan)
            else:
                print("Saldo Anda Tidak mencukupi")
    if option == 3:
        print("Sisa Saldo Anda :", saldo)
else :
    print("Pin yang anda masukkan salah!")
    print("Saldo anda tidak cukup")