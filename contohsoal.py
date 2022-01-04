harga_tanah_permeter = 300000
beli_tanah = int(input('Luas tanah berapa M^2 : '))
harga = harga_tanah_permeter * beli_tanah
if harga >= 50000000 and harga < 100000000 :
    pajak = 3/100
elif harga >= 100000000 :
    pajak = 5/100
else :
    pajak = 1/100

total_pajak = harga * pajak
uang_bersih = harga - total_pajak
print('Total pajak : ',total_pajak)
print('Harga jual sblm kena pajak : ', harga)
print('Total Harga jual sudah dikenakan pajak : ',uang_bersih)