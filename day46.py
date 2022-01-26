#Profil
print('='*60)
print("Laundry Kilat Bu Fima".center(60," "))
print('='*60,"\n")
print('-'*60)
print("Input Data Pesanan".center(60," "))
print('-'*60)
#Inputan
namaPelanggan = input('Nama Pelanggan\t\t\t: ')
alamat = input('Alamat\t\t\t\t: ')
noHp = int(input('No Handphone\t\t\t: '))
print('-'*60)
print('Kategori Cucian'.center(60," "))
print('-'*60)
kategori = ['1. Cuci Biasa','2. Plus Setrika','3. Cuci Kilat']
for i in kategori:
    print(i)
print('-'*60)
pilihanKat = int(input("Input No Kategori (1-3)\t\t: "))
beratCucian = int(input("Berat Cucian <Kg>\t\t: "))

#Proses
proses = 0
if beratCucian > 10 and beratCucian <= 20:
    proses += 2
elif beratCucian <= 10 :
    proses += 1
else :
    proses += 3

hargaCuciBiasa = 5000
hargaCuciSetrika = 7000
hargaCuciKilat = 6000

#output dan TotalBiaya
def nmr1():
    print("Cuci Biasa",proses,"hari\t\t: Rp.",hargaCuciBiasa)
def nmr2():
    print("Cuci plus Setrika",proses,"hari\t: Rp.",hargaCuciSetrika)
def nmr3():
    print("Cuci Kilat",proses,"hari\t\t: Rp.", hargaCuciKilat)

#output RESI
print('-'*60)
print('Resi Pesanan Laundry'.center(60," "))
print('-'*60)
print("Nama Pelanggan\t\t\t: ",namaPelanggan)
print('Alamat\t\t\t\t: ',alamat)
print('No Handphone\t\t\t: ', noHp)

if pilihanKat == 1 :
    nmr1()
    totalBiaya = beratCucian*hargaCuciBiasa
elif pilihanKat == 2 :
    nmr2()
    totalBiaya = beratCucian*hargaCuciSetrika
elif pilihanKat == 3 :
    nmr3()
    totalBiaya = beratCucian*hargaCuciKilat

print('Total biaya\t\t\t: Rp.',totalBiaya)
print('='*60)
bayar = int(input('Total Bayar\t\t\t: '))
kembalian = bayar-totalBiaya
print('Kembalian\t\t\t: Rp.',kembalian)
print('-'*60)
print("Terimakasih Telah Datang di Laundri Kami")
