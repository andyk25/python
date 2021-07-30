# задача 1
# _*_ coding: utf8 # включить кодировку utf8
import time

class TrafficLight:


    def __init__(self):
        self.__color = "красный"
        self.__timer = 7


    def running(self):
        if self.__color == "красный":
            self.__color = "желтый"
            self.__timer = 2
        elif self.__color == "желтый":
            self.__color = "зеленый"
            self.__timer = 9
        else:
            self.__color = "красный"
            self.__timer = 7
        print(self.__color)
        time.sleep(self.__timer)
        


tl = TrafficLight()
for i in range(6):
    tl.running()
