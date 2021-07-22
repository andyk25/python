# урок 5 задача 2

with open('text2.txt', 'r', encoding='utf-8') as f:
    for indx, line in enumerate(f):
        print(f"{indx+1} строка  - {line.count(' ')+1} слов(а)")

print(f"всего {indx+1} строк")
