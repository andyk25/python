# решение чз список
months = {1: "зима", 2: "зима", 3: "весна", 4: "весна", 5: "весна", 6: "лето", 7: "лето",
          8: "лето", 9: "осень", 10: "осень", 11: "осень", 12: "зима"}
stroka = '1'
while stroka != '':
    stroka = input("Введите месяц : ")
    month = int(stroka) if stroka.isdigit() else 0
    print(f"Это {months.get(month, 'нет такого месяца')}")
