import random

print('''1. gunting
2. batu
3. kertas''')
b = int(input("masukan angka 1-3: "))
if b == 1:
    print("anda memilih gunting")
elif b == 2:
    print("anda memilih batu")
elif b == 3:
    print("anda memilih kertas")
else:
    print("anda salah memasukan angka")
a = random.randint(1, 4)
if a == 1:
    print("bot memilih gunting")
elif a == 2:
    print("bot memilih batu")
elif a == 3:
    print("bot memilih kertas")

if b == a :
    print("seri")
elif b == 1 and a == 3 or b == 2 and a == 1 or b == 3 and a == 2:
    print("anda menang")
else :
    print("anda kalah")