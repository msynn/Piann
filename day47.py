#Mengurutkan list memakai selection sort
print('='*40)
print("Selection sort".center(40," "))
print('='*40)
list = []
ulang = int(input("Total List : "))
for i in range(ulang) :
    list2 = int(input('Masukkan angka :'))
    list.append(list2)

def ss(list):
    iterasi = 0
    for i in range(len(list)-1):
        minimal = i
        for j in range(i+1,len(list)):
            if list[j] < list[minimal]:
                minimal = j
        iterasi += 1
        list[i],list[minimal] = list[minimal], list[i]
        print(iterasi, list)


print("Data yang akan di sort\t:",list)
print('Seection sort :')
ss(list)

