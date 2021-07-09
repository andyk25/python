# задача 4
str = input("введите целое положительное число : ")
maximum = int(str[0])
for x in range(1,len(str)):
    current_number = int(str[x:x+1])
    if  current_number > maximum :
        maximum = current_number
print(f"максимальная цифра равна : {maximum}")
