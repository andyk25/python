# Для чисел в пределах от 20 до 240 найти числа, кратные 20 или 2
numbers = [i for i in range(20, 241) if i % 20 == 0 or i % 21 == 0]
print(*numbers)
