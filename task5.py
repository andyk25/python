# урок 3 задача 5
def summ():
    summ = 0
    while True:
        numbers = input("введите числа чз пробел : ").split()
        for elm in numbers:
            if elm.isdigit():
                summ += int(elm)
            else:
                print(f"сумма = {summ}")
                return
        print(f"сумма = {summ}")

summ()