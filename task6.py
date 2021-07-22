# урок 5 задача 6
learns = dict()
with open('text6.txt', 'r', encoding='utf-8') as txt:
    for elm in txt:
        summ = 0
        for i in elm.split():
            indx = i.find("(")
            summ += int(('0', i[:indx])[indx != -1])
        learns[elm.split()[0]] = summ
print(learns)
