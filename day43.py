print("PROGRAM PINJAMAN KOPERASI BULANAN\n")
pinjaman = int(input("Masukkan Pinjaman : "))
print("==>")
waktuPelunasan = int(input("Total Waktu bulan pelunasan (10/20/24) : "))
if waktuPelunasan == 10 or waktuPelunasan == 20 or waktuPelunasan == 24 :
    waktuPelunasan = waktuPelunasan
    print("=================================>\n")
else :
    waktuPelunasan = 0
    print("===> Maaf, Kami tidak melayani jangka waktu pinjaman tersebut!")
total = []
bunga = 0
for i in range (waktuPelunasan):
    i+=1
    if waktuPelunasan == 10 :
        bunga += 0.007
    elif waktuPelunasan == 20 :
        bunga += 0.005
    elif waktuPelunasan == 24 :
        bunga += 0.004
    uangBunga = pinjaman*bunga
    uangBagi = pinjaman/waktuPelunasan
    BayarPerBulan = uangBagi+uangBunga
    total.append(BayarPerBulan)
    print(f"Total Bayar bulan ke- {i} adalah : ")
    print("Rp.",BayarPerBulan)
    print("============================>")

print("Jumlah yang harus di bayar :",sum(total))