# урок 2 задача 6
goods = []
title = "non empty"
while True:
    title = input("Введите название :")
    price = input("Введите цену :")
    numberof = input("Введите количество :")
    unit = input("Введите eдиницу измерения :")
    if title =="" or price =="" or numberof == "" or unit == "": break
    goods.append(({'название':title},
    {'цена':price},
    {'количество':numberof},
    {'единицы':unit}))
results = {}

for good in goods:
    for elm in good:
        for key,val in elm.items():
            if results.get(key) :  results[key] = results[key] + [val]
            else: results[key] = [val]
for key,val in results.items():
    print(key,*set(val))
