# урок 5 задача 1

with open('text.txt', 'w', encoding='utf-8') as f:
    stroka = " fill"
    while stroka != "":
        stroka = input("Введите текст : ")
        f.write(stroka + "\n")

with open("text.txt", 'r', encoding='utf-8') as f:
    print(f.read())
