# Contoh soal penginputan 3 nilai  dan penginputan minat jurusan
# Jika nilai rata-rata dibawah 70 maka dinyatakan tidak lulus, jika nilai rata-rata 70 maka akan lolos dengan jurusan yang dia pilih, jika nilai diatas 70 maka bebas memilih jurusan yang ia sukai.
print("Penginputan Nilai")
mtk = int(input('Nilai MTK : '))
b_ing = int(input('Nilai Bahasa Inggris : '))
bind = int(input('Nilai Bahasa Indonesia : '))
rata2_nilai = (mtk + b_ing + bind) / 3
print('Pilihan Bidang')
bidang = ['1. Elektro', '2. Mesin', '3. Pariwisata']
for i in bidang :
    print(i)
minat = int(input('Masukkan kode Jurusan yang anda minati : '))
if rata2_nilai < 70 :
    print('Anda Dinyatakan tidak lolos karena Skor anda =', rata2_nilai)
elif rata2_nilai == 70 :
    if minat == 1 :
        bidang = 'Teknik Elektro'
    elif minat == 2 :
        bidang = 'Teknik Mesin'
    else :
        bidang = 'Bidang Pariwisata'
    print("Skor anda adalah", rata2_nilai, ', anda dinyatakan Lulus ke bidang berikut :', bidang)
elif rata2_nilai > 70 and rata2_nilai <= 100 :
    print('Anda Bebas Memilih jurusan yang disukai')
