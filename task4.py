# урок 5 задача 4
en2rus = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}
rtxt = open('rustext.txt', 'w', encoding='utf-8')
with open('text4.txt', 'r', encoding='utf-8') as txt:
    for line in txt:
        rtxt.write(line.replace(line.split()[0], en2rus[line.split()[0]]))
rtxt.close()

with open('rustext.txt', 'r', encoding='utf-8') as rtxt:
    print(rtxt.read())
