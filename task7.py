# урок 5 задача 7
import json
firms = dict()
firms_av = []
summ = 0
with open('text7.txt', 'r', encoding='utf-8') as txt:
    for num, elm in enumerate(txt):
        prib = int(elm.split()[2]) - int(elm.split()[3])
        if prib > 0:
            summ += prib
        firms[elm.split()[0]] = prib

firms_av.append(firms)
firms_av.append({"average_profit": summ/(num+1)})
with open("text7.json", "w") as fjs:
    json.dump(firms_av, fjs)
