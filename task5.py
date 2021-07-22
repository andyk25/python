# урок 5 задача 5
import random
summ = 0
with open('text5.txt', 'w', encoding='utf-8') as txt:
    for i in range(10):
        num = int(random.uniform(1, 100))
        summ += num
        txt.write(str(num) + ' ')

print(f"Сумма чисел = {summ}")
