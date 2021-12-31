nama = input('Masukkan nama anda\t : ')
jumlah_anak = int(input('Jumlah Anak\t\t : '))
gaji = int(input('Masukkan gaji pokok anda : '))
tunjangan_istri = 20/100
tot_tunjangan_istri = tunjangan_istri * gaji

tunjangan_anak = 5/100 * jumlah_anak
total_tunjangan_anak = tunjangan_anak * gaji

total_tunjangan = total_tunjangan_anak + tot_tunjangan_istri
gaji_kotor = gaji + total_tunjangan

pajak = 10/100
total_pajak = gaji_kotor * pajak
gaji_bersih = gaji_kotor - total_pajak

print('\nNote\n')
print('Nama\t\t\t: ', nama)
print('Total tunjangan\t\t: ', total_tunjangan)
print('Total gaji bersih\t:', gaji_bersih)