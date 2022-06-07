# -*- coding: utf-8 -*-
"""
Задание 11.1

Создать функцию parse_cdp_neighbors, которая обрабатывает
вывод команды show cdp neighbors.

У функции должен быть один параметр command_output, который ожидает как аргумент
вывод команды одной строкой (не имя файла). Для этого надо считать все содержимое
файла в строку, а затем передать строку как аргумент функции (как передать вывод
команды показано в коде ниже).

Функция должна возвращать словарь, который описывает соединения между устройствами.

Например, если как аргумент был передан такой вывод:
R4>show cdp neighbors

Device ID    Local Intrfce   Holdtme     Capability       Platform    Port ID
R5           Fa 0/1          122           R S I           2811       Fa 0/1
R6           Fa 0/2          143           R S I           2811       Fa 0/0

Функция должна вернуть такой словарь:

    {("R4", "Fa0/1"): ("R5", "Fa0/1"),
     ("R4", "Fa0/2"): ("R6", "Fa0/0")}

В словаре интерфейсы должны быть записаны без пробела между типом и именем.
То есть так Fa0/0, а не так Fa 0/0.

Проверить работу функции на содержимом файла sh_cdp_n_sw1.txt. При этом функция должна
работать и на других файлах (тест проверяет работу функции на выводе
из sh_cdp_n_sw1.txt и sh_cdp_n_r3.txt).

Ограничение: Все задания надо выполнять используя только пройденные темы.
"""

# Напишите здесь свой код :-)
from pprint import pprint
def parse_cdp_neighbors(command_output):
    out = {}
    Env = ''
    for line in command_output.split('\n'):
        #if line and line.find('show cdp neighbors') != -1:
        if '>' in line: 
            Env = list(line.split('>'))[0]
        #print('='*30)
        #pprint(line)
        #elif line and (line.startswith('R') or line.startswith('SW')) and line[1].isdigit():
        elif len(line.split()) >= 5 and line.split()[3].isdigit():
            hostname, intname, intnum, *other, intnameleft, intnumleft = line.split()
            out[(Env, intname + intnum)] = (hostname, intnameleft + intnumleft)
            ####out = {Env:str(line.split()[-2]+line.split()[-1]),line.split()[0]:1}
            #out.update({(Env,str(line.split()[-2]+line.split()[-1])):(line.split()[0],line.split()[1]+line.split()[2])})
    return out#command_output.split('\n')
#,:str(line.split()[1]+line.split()[2]




if __name__ == "__main__":
    with open("sh_cdp_n_sw1.txt") as f:
        pprint(parse_cdp_neighbors(f.read()))


