print('=======Penghitungan IPK=======')
nama = input('Nama : ')
nim = input('Nim : ')
jumlahmatkul = int(input('Jumlah Mata Kuliah : '))
print(20*'=','\n')
listBobotMK = [] 
listSKS = []

for i in range (0,jumlahmatkul):
    namaMatkul = input('Nama mata Kuliah : ') 
    sks = int(input('Total SKS : '))
    nilai = int(input('Masukkan Nilai : '))
    if nilai >= 80 and nilai <= 100 :
        listBobotMK.append(4*sks)
        predikat = 'A'
    elif nilai >= 65 and nilai < 80 :
        listBobotMK.append(3*sks)
        predikat = 'B'
    elif nilai >= 55 and nilai < 65 :
        listBobotMK.append(2*sks)
        predikat = 'C'
    else :
        listBobotMK.append(0*sks)
        predikat = 'D'
    listSKS.append(sks)

    print('Predikat Matakuliah',namaMatkul,' : ',predikat)
    print('='*20,'\n')

totalBobotMK = sum(listBobotMK)
totalSKS = sum(listSKS)
ipk = totalBobotMK/totalSKS

if ipk >= 3.5 and ipk >= 4 :
    print('PREDIKAT DENGAN PUJIAN')
elif ipk >= 3 and ipk < 3.5 :
    print('PREDIKAT SANGAT MEMUASKAN')
elif ipk >= 2.5 and ipk < 3 :
    print('PREDIKAT MEMUASKAN')
else :
    print('PEDIKAT LULUS')

print('Dengan nilai IPK : ', ipk)


