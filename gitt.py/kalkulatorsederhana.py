print('='*20, "KALKULATOR SEDERHANA", '='*20)
a = float(input("Masukan Angka :"))
operator = input("Masukan Operator [*,/,+,-] :")
b = float(input("Masukan Angka :"))
perkalian = a * b
pembagian = a / b
pengurangan = a - b
penambahan = a + b

if operator == '*' :
    print("Hasil dari",a,"*", b, '=', perkalian)
elif operator == '/' :
    print("Hasil dari",a,'/',b,'=', pembagian)
elif operator == '-' :
    print("Hasil dari",a,'-',b,'=', pengurangan)
elif operator == '+' :
    print("Hasil dari",a,'+',b,'=',penambahan)
else:
    print("Maaf kamu salah memasukan operator bilangan")