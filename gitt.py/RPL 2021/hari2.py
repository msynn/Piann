print('='*10,"MAS YANN SHOP",'='*10)
total_belanja = int(input("Masukkan total belanja :"))
kode_hari = input("Masukkan kode hari :")
diskon = [1,2,3,4,5,6,10]
if kode_hari == "senin":
    a = diskon[0]
    discount = total_belanja * a/100
elif kode_hari == "selasa":
    a = diskon[1]
    discount = total_belanja * a/100
elif kode_hari == "rabu":
    a = diskon[2]
    discount = total_belanja * a/100
elif kode_hari == "kamis":
    a = diskon[3]
    discount = total_belanja * a/100
elif kode_hari == "jumat":
    a = diskon[4]
    discount = total_belanja * a/100
elif kode_hari == "sabtu":
    a = diskon[5]
    discount = total_belanja * a/100
elif kode_hari == "minggu":
    a = diskon[6]
    discount = total_belanja * a/100
else:
    print("Kode anda tidak berlaku")

pay = total_belanja - discount
print("discount hari ini :",a ,'%')
print("jumlah discount : Rp.", discount)
print("Total yang harus anda bayar : Rp.", pay)

