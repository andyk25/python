# задача 3
# _*_ coding: utf8 # включить кодировку utf8

class Worker:

    def __init__(self, name="Сан", surname="Саныч", position="сотрудник", wage=10000, bonus=10000):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": wage, "bonus": bonus}


class Position(Worker):


    def get_full_name(self):
        return self.name + " " + self.surname


    def get_total_income(self):
        return self._income["wage"] + self._income["bonus"]


workers = []
workers.append(Position("Анна", "Алексеевна", "бухгалтер", 40000, 30000))
workers.append(Position("Артем", "Иванович", "сисадмин", 50000, 40000))
workers.append(Position("Света", "Демидовна", "кадровик", 20000, 10000))

for elm in workers:
    print(f"{elm.get_full_name()}, должность : {elm.position}, доход : {elm.get_total_income()}")
