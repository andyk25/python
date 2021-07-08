# задача 4
str = input("введите целое положительное число : ")
maximum = int(str[0])
for x in range(1,len(str)):
    if int(str[x:x+1]) > maximum :
        maximum = int(str[x:x+1])
print (f"максимальная цифра равна : {maximum}")
