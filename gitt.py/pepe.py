number = [2,54,38,76,23,56,84,90]

for i in range(len(number)-1,0,-1):
    for j in range(i):
        if number[j]<number[j+1]:
            fyan = number[j]
            number[j]=number[j+1]
            number[j+1]=fyan

print(number)