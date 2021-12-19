print('='*7, "PROGRAM MENGUBAH SATUAN PANJANG", '='*7)
print('='*15, "FYAN RAMADHAN", '='*15)
nilai_a = int(input("Masukkan Nilai :"))
print("MASUKKAN SATUAN METER DENGAN BENAR")
operator_perbandingan = input("Masukkan satuan panjang (mm,cm,dm,m,dam,hm,km) :")
operator_perbandingan2 = input("Ubah ke satuan (mm,cm,dm,m,dam,hm,km) :")

operator_perbandingan = operator_perbandingan.lower()
operator_perbandingan2 = operator_perbandingan2.lower()

if operator_perbandingan == 'mm' and operator_perbandingan2 == 'cm':
    print("Nilai", nilai_a, operator_perbandingan,"jika di convert ke", operator_perbandingan2, '=', nilai_a/10)
elif operator_perbandingan == 'mm' and operator_perbandingan2 == 'dm':
    print("Nilai", nilai_a, operator_perbandingan,"jika di convert ke", operator_perbandingan2, '=', nilai_a/100)
elif operator_perbandingan == 'mm' and operator_perbandingan2 == 'm':
    print("Nilai", nilai_a, operator_perbandingan,"jika di convert ke", operator_perbandingan2, '=', nilai_a/1000)
elif operator_perbandingan == 'mm' and operator_perbandingan2 == 'dam':
    print("Nilai", nilai_a, operator_perbandingan,"jika di convert ke", operator_perbandingan2, '=', nilai_a/10000)
elif operator_perbandingan == 'mm' and operator_perbandingan2 == 'hm':
    print("Nilai", nilai_a, operator_perbandingan,"jika di convert ke", operator_perbandingan2, '=', nilai_a/100000)
elif operator_perbandingan == 'mm' and operator_perbandingan2 == 'km':
    print("Nilai", nilai_a, operator_perbandingan,"jika di convert ke", operator_perbandingan2, '=', nilai_a/1000000)
elif operator_perbandingan == 'cm' and operator_perbandingan2 == 'dm':
    print("Nilai", nilai_a, operator_perbandingan,"jika di convert ke", operator_perbandingan2, '=', nilai_a/10)
elif operator_perbandingan == 'cm' and operator_perbandingan2 == 'm':
    print("Nilai", nilai_a, operator_perbandingan,"jika di convert ke", operator_perbandingan2, '=', nilai_a/100)
elif operator_perbandingan == 'cm' and operator_perbandingan2 == 'dam':
    print("Nilai", nilai_a, operator_perbandingan,"jika di convert ke", operator_perbandingan2, '=', nilai_a/1000)
elif operator_perbandingan == 'cm' and operator_perbandingan2 == 'hm':
    print("Nilai", nilai_a, operator_perbandingan,"jika di convert ke", operator_perbandingan2, '=', nilai_a/10000)
elif operator_perbandingan == 'cm' and operator_perbandingan2 == 'km':
    print("Nilai", nilai_a, operator_perbandingan,"jika di convert ke", operator_perbandingan2, '=', nilai_a/100000)
elif operator_perbandingan == 'dm' and operator_perbandingan2 == 'm':
    print("Nilai", nilai_a, operator_perbandingan,"jika di convert ke", operator_perbandingan2, '=', nilai_a/10)
elif operator_perbandingan == 'dm' and operator_perbandingan2 == 'dam':
    print("Nilai", nilai_a, operator_perbandingan,"jika di convert ke", operator_perbandingan2, '=', nilai_a/100)
elif operator_perbandingan == 'dm' and operator_perbandingan2 == 'hm':
    print("Nilai", nilai_a, operator_perbandingan,"jika di convert ke", operator_perbandingan2, '=', nilai_a/1000)
elif operator_perbandingan == 'dm' and operator_perbandingan2 == 'km':
    print("Nilai", nilai_a, operator_perbandingan,"jika di convert ke", operator_perbandingan2, '=', nilai_a/10000)
elif operator_perbandingan == 'm' and operator_perbandingan2 == 'dam':
    print("Nilai", nilai_a, operator_perbandingan,"jika di convert ke", operator_perbandingan2, '=', nilai_a/10)
elif operator_perbandingan == 'm' and operator_perbandingan2 == 'hm':
    print("Nilai", nilai_a, operator_perbandingan,"jika di convert ke", operator_perbandingan2, '=', nilai_a/100)
elif operator_perbandingan == 'm' and operator_perbandingan2 == 'km':
    print("Nilai", nilai_a, operator_perbandingan,"jika di convert ke", operator_perbandingan2, '=', nilai_a/1000)
elif operator_perbandingan == 'dam' and operator_perbandingan2 == 'hm':
    print("Nilai", nilai_a, operator_perbandingan,"jika di convert ke", operator_perbandingan2, '=', nilai_a/10)
elif operator_perbandingan == 'dam' and operator_perbandingan2 == 'km':
    print("Nilai", nilai_a, operator_perbandingan,"jika di convert ke", operator_perbandingan2, '=', nilai_a/100)
elif operator_perbandingan == 'hm' and operator_perbandingan2 == 'km':
    print("Nilai", nilai_a, operator_perbandingan,"jika di convert ke", operator_perbandingan2, '=', nilai_a/10)
elif operator_perbandingan == 'km' and operator_perbandingan2 == 'hm':
    print("Nilai", nilai_a, operator_perbandingan,"jika di convert ke", operator_perbandingan2, '=', nilai_a*10)
elif operator_perbandingan == 'km' and operator_perbandingan2 == 'dam':
    print("Nilai", nilai_a, operator_perbandingan,"jika di convert ke", operator_perbandingan2, '=', nilai_a*100)
elif operator_perbandingan == 'km' and operator_perbandingan2 == 'm':
    print("Nilai", nilai_a, operator_perbandingan,"jika di convert ke", operator_perbandingan2, '=', nilai_a*1000)
elif operator_perbandingan == 'km' and operator_perbandingan2 == 'dm':
    print("Nilai", nilai_a, operator_perbandingan,"jika di convert ke", operator_perbandingan2, '=', nilai_a*10000)
elif operator_perbandingan == 'km' and operator_perbandingan2 == 'cm':
    print("Nilai", nilai_a, operator_perbandingan,"jika di convert ke", operator_perbandingan2, '=', nilai_a*100000)
elif operator_perbandingan == 'km' and operator_perbandingan2 == 'mm':
    print("Nilai", nilai_a, operator_perbandingan,"jika di convert ke", operator_perbandingan2, '=', nilai_a*1000000)
elif operator_perbandingan == 'hm' and operator_perbandingan2 == 'dam':
    print("Nilai", nilai_a, operator_perbandingan,"jika di convert ke", operator_perbandingan2, '=', nilai_a*10)
elif operator_perbandingan == 'hm' and operator_perbandingan2 == 'm':
    print("Nilai", nilai_a, operator_perbandingan,"jika di convert ke", operator_perbandingan2, '=', nilai_a*100)
elif operator_perbandingan == 'hm' and operator_perbandingan2 == 'dm':
    print("Nilai", nilai_a, operator_perbandingan,"jika di convert ke", operator_perbandingan2, '=', nilai_a*1000)
elif operator_perbandingan == 'hm' and operator_perbandingan2 == 'cm':
    print("Nilai", nilai_a, operator_perbandingan,"jika di convert ke", operator_perbandingan2, '=', nilai_a*10000)
elif operator_perbandingan == 'hm' and operator_perbandingan2 == 'mm':
    print("Nilai", nilai_a, operator_perbandingan,"jika di convert ke", operator_perbandingan2, '=', nilai_a*100000)
elif operator_perbandingan == 'dam' and operator_perbandingan2 == 'm':
    print("Nilai", nilai_a, operator_perbandingan,"jika di convert ke", operator_perbandingan2, '=', nilai_a*10)
elif operator_perbandingan == 'dam' and operator_perbandingan2 == 'dm':
    print("Nilai", nilai_a, operator_perbandingan,"jika di convert ke", operator_perbandingan2, '=', nilai_a*100)
elif operator_perbandingan == 'dam' and operator_perbandingan2 == 'cm':
    print("Nilai", nilai_a, operator_perbandingan,"jika di convert ke", operator_perbandingan2, '=', nilai_a*1000)
elif operator_perbandingan == 'dam' and operator_perbandingan2 == 'mm':
    print("Nilai", nilai_a, operator_perbandingan,"jika di convert ke", operator_perbandingan2, '=', nilai_a*10000)
elif operator_perbandingan == 'm' and operator_perbandingan2 == 'dm':
    print("Nilai", nilai_a, operator_perbandingan,"jika di convert ke", operator_perbandingan2, '=', nilai_a*10)
elif operator_perbandingan == 'm' and operator_perbandingan2 == 'cm':
    print("Nilai", nilai_a, operator_perbandingan,"jika di convert ke", operator_perbandingan2, '=', nilai_a*100)
elif operator_perbandingan == 'm' and operator_perbandingan2 == 'mm':
    print("Nilai", nilai_a, operator_perbandingan,"jika di convert ke", operator_perbandingan2, '=', nilai_a*1000)
elif operator_perbandingan == 'dm' and operator_perbandingan2 == 'cm':
    print("Nilai", nilai_a, operator_perbandingan,"jika di convert ke", operator_perbandingan2, '=', nilai_a*10)
elif operator_perbandingan == 'dm' and operator_perbandingan2 == 'mm':
    print("Nilai", nilai_a, operator_perbandingan,"jika di convert ke", operator_perbandingan2, '=', nilai_a*100)
elif operator_perbandingan == 'cm' and operator_perbandingan2 == 'mm':
    print("Nilai", nilai_a, operator_perbandingan,"jika di convert ke", operator_perbandingan2, '=', nilai_a*10)

else:
    print("mohon Masukkan satuan dengan benar")