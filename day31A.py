print('MENGHITUNG GAJI KARYAWAN\n')

print('Golongan :')
gol = ['Gol 1.', 'Gol 2.', 'Gol 3.']
for i in gol :
    print(i)
gol_pilihan = int(input('Masukkan kode Golongan : '))

if gol_pilihan == 1 :
    gaji = 1500000
elif gol_pilihan == 2 :
    gaji = 1200000
elif gol_pilihan == 3 :
    gaji = 1000000
else :
    print('Kode Golongan tidak valid')

tahunIni = 2011
TahunMasukKerja = int(input('Tahun Masuk Kerja : '))
totalKerja = tahunIni - TahunMasukKerja

if totalKerja >= 7 :
    bonus = 150000
else :
    bonus = 0

totalGaji = gaji + bonus

print('Total Gaji + bonus anda adalah : ', totalGaji)