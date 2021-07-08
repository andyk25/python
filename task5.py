# задача 5
vyruchka = int(input("введите выручку : "))
izderzhki = int(input("введите издержки : "))
if vyruchka > izderzhki :
    print ("фирма работает c прибылью ")
    print (f"рентабельность выручки : {(vyruchka - izderzhki) / vyruchka}")
    empls = int(input("сколько сотрудников работает на фирме ? "))
    print(f"прибыль фирмы в расчете на одного сотрудника : {(vyruchka - izderzhki) / empls}")
else :
    print ("фирма работает в убыток")
