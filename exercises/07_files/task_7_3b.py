# -*- coding: utf-8 -*-
"""
Задание 7.3b

Сделать копию скрипта задания 7.3a.

Переделать скрипт:
- Запросить у пользователя ввод номера VLAN.
- Выводить информацию только по указанному VLAN.

Пример работы скрипта:

Enter VLAN number: 10
10       0a1b.1c80.7000      Gi0/4
10       01ab.c5d0.70d0      Gi0/8

Ограничение: Все задания надо выполнять используя только пройденные темы.

"""
position = 0 
vl_inp = input('Enter vlan number: ')
stroke = 0
li_list = []
with open('CAM_table.txt') as file:
    source = file.read().split()
    for word in source:
        position += 1
        if word and word == 'DYNAMIC' and position > 3:
            #for i as range(3):
            #li_list[stroke][position-3],li_list[stroke][position-2],li_list[stroke][position] = source[position-3],source[position-2],source[position]
            li_list.append([int(source[position-3]),source[position-2],source[position]])
            stroke += 1
            #print(f'{source[position-3]:8}{source[position-2]:20}{source[position]}')
#print(sorted(li_list))
for line in sorted(li_list):
    if line[0] == int(vl_inp):
        print(f'{line[0]:<8}{line[1]:20}{line[2]}')

