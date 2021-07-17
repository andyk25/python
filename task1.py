# урок 4 задача 1
from sys import argv


def raschet_zp(work_time, work_stavka, work_prem):
    #   вычисляем зп сотрудника = выработка в часах * ставка в час) + премия
    return (work_time * work_stavka) + work_prem


script_name, work1_time, work1_stavka, work1_prem = argv
print(raschet_zp(int(work1_time), int(work1_stavka), int(work1_prem)))
