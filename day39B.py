n = int(input('Masukkan angka : '))

for i in range(1, n+1):
    for j in range(1, n+1):
        print(j, end='')
    print()
    n-=1