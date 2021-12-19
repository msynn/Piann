list = [2,54,38,76,23,56,84,90]
print("Data yang akan di sort", list)
print("Insertion sort :")

for j in range(len(list)-1,-1,-1):
    value = list[j]
    hole = j
    while hole <(len(list)-1) and list[hole+1]>list[hole]:
        list[hole] = list[hole+1]
        hole = hole+1
        list[hole] = value
    print(list)