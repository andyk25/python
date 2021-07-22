# урок 5 задача 3

with open('text3.txt', 'r', encoding='utf-8') as f:
    summ = 0
    for indx, line in enumerate(f):
        zp = int(line.split()[1])
        summ += zp
        if zp < 20000:
            print(line.split()[0])
print(f"средних доход сотрудников :  {round(summ/(indx+1)/1000,3)} тыс. руб.")
