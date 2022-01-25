print("fungsi dengan return value".center(50,'='))
def kuadrat(argumen):
    total = argumen**2
    print(f"Nilai kuadrat dari {argumen} adalah", total)
    return total

a = kuadrat(9)
print(a)

print("fungsi".center(50,'='))

#Tambah

def tambah(angka1, angka2):
    hasil = angka1 + angka2
    print(angka1, "+", angka2, "=", hasil)
    return hasil


print(50*'=')
#perkalian

def kali(angka1, angka2):
    hasil = angka1 * angka2
    print(angka1, "*", angka2, "=", hasil)
    return hasil

b = kali(11,tambah(10,9))