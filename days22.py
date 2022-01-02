#Tentukan jumlah harga saka semen jika harga 1 sak 50.000
# Jika membeli maksimal 100 sak dpt potongan harga 2,5%,
# Jika membeli diatas 200 sak maka mendapat diskon 10%.
print("===========SEMEN====a=====\n")
print("Harga 1 sak semen = 50.000")
harga_semen = 50000
beli_semen = int(input("Masukkan Total semen yang dibeli :"))
diskon100 = 2.5/100
diskon200 = 10/100
total = harga_semen * beli_semen
if beli_semen >= 100 and beli_semen < 200 :
    diskon = total * diskon100
    hargaTotal = total - diskon
elif beli_semen >= 200 :
    diskon = total * diskon200
    hargaTotal = total - diskon
else:
    hargaTotal = total

print("Total Harga semen = ", hargaTotal)
