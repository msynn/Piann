print('='*10,'DIAMOND MOBILE LEGEND','='*10)
id = 112233
server = 2123
id2 = True
server2 = True
nick = "Mas Yann"
harga_dm = 500

while id2 == True :
    id_masukan = int(input("Masukkan id : "))
    if id_masukan == id :
        id2 = False
    else :
        print("ID yang anda masukkan salah!")

while server2 == True :
    server_masukan = int(input("Masukkan Server : "))
    if server_masukan == server :
        server2 = False
    else :
        print("Server yang anda masukkan salah!")

if id2 == False and server2 == False :
    print("Selamat datang ", nick)
    dm = [50,100,150,200,250,300]
    for i in dm :
        print(i,"Diamond", "harga = ", i*harga_dm)
beli = int(input("Masukkan Jumlah Top Up : "))
if beli == dm[0]:
    total = dm[0]*harga_dm
elif beli == dm[1]:
    total = dm[1]*harga_dm
elif beli == dm[2]:
    total = dm[2]*harga_dm
elif beli == dm[3]:
    total = dm[3]*harga_dm
elif beli == dm[4]:
    total = dm[4]*harga_dm
elif beli == dm[5]:
    total = dm[5]*harga_dm
else :
    print('Masukkan Diamon yang benar!')
print('Total bayar', total)