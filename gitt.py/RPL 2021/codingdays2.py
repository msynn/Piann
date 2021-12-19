gaji_bulanan = 5000000
keterangan_alpa = int(input("berapa kali anda tidak hadir(tanpa Keterangan) :"))
pajak = 2.5/100
if keterangan_alpa > 5:
    potongan_gaji_kehadiran = 25000 * keterangan_alpa
    gaji_kotor = gaji_bulanan - potongan_gaji_kehadiran
    total_pajak = gaji_kotor * pajak
    total_gaji_bersih = gaji_kotor - total_pajak
else:
    total_pajak = gaji_bulanan * pajak
    total_gaji_bersih = gaji_bulanan - total_pajak

print("Gaji Bulanan      : Rp.", gaji_bulanan)
print("Total Gaji Bersih : Rp.", total_gaji_bersih)

