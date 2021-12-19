nama = input("Masukkan nama anda : ")
umur = int(input("Masukkan umur anda : "))
tinggi = int(input("Berapa tinggi anda : "))
menikah = input("status 'sudah menikah' atau 'belum menikah' :")
if menikah == 'sudah menikah':
    print(True)
elif menikah == 'belum menikah':
    print(False)
else:
    print('''Maaf status anda belum jelas.
    silahkan masukkan :
    sudah menikah
    belum menikah''')