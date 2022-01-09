pekerjaan = input('Masukkan Pekerjaan : ')
anak = int(input('Jumlah anak : '))
gaji = int(input('Masukkan gaji : '))

if gaji > 3000000 and gaji <  7000000:
    pajak = 5/100    
    if pekerjaan == 'PNS' :
        pajak = pajak + 2/100

elif gaji >= 7000000 :
    pajak = 10/100
    if pekerjaan == 'PNS' :
        pajak = pajak + 2/100
else :
    pajak = 0

if anak >= 2 :
    tunjangan = 10/100
else:
    tunjangan = 0

tot_pajak = gaji * pajak
gaji_pajak = gaji - tot_pajak
tot_tunjangan = gaji * tunjangan
gaji_bersih = gaji_pajak + tot_tunjangan

print('Pekerjaan \t\t : ', pekerjaan)
print('total gaji bersih \t :', gaji_bersih)
print('Total Tunjangan \t :', tot_tunjangan)
print('Total Pajak   \t \t: ', tot_pajak)