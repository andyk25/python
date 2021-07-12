# урок 2 задача 5
rating = [7, 5, 3, 3, 2]
num = 1
while num != -1:
    num = int(input("Введите натуральное число :"))
    for indx, elm in enumerate(rating):
        if num > elm:
            rating.insert(indx,num)
            break
    else : rating.append(num)
    if num < 0 : break
    print(*rating,sep = ',')
