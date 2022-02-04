import calendar

yy = int(input("Tahun : "))
mm = int(input("Bulan : "))
print("\n -----Kalender-----\n")

print(calendar.month(yy,mm))


import random

n = random.randint(10,100)
print("Angka acak yang keluar adalah : ",n)