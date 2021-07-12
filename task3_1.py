months = ["зима", "весна", "лето", "осень", "зима"]
stroka = '1'
while stroka != '':
    stroka = input("Введите месяц : ")
    month = int(stroka) if stroka.isdigit() else 0
    print(("нет такого месяца", f"Это {months[month // 3]}")[0 < month < 13])
