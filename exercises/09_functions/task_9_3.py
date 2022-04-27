# -*- coding: utf-8 -*-
"""
Задание 9.3

Создать функцию get_int_vlan_map, которая обрабатывает конфигурационный
файл коммутатора и возвращает кортеж из двух словарей:
* словарь портов в режиме access, где ключи номера портов,
  а значения access VLAN (числа):
{'FastEthernet0/12': 10,
 'FastEthernet0/14': 11,
 'FastEthernet0/16': 17}

* словарь портов в режиме trunk, где ключи номера портов,
  а значения список разрешенных VLAN (список чисел):
{'FastEthernet0/1': [10, 20],
 'FastEthernet0/2': [11, 30],
 'FastEthernet0/4': [17]}

У функции должен быть один параметр config_filename, который ожидает как аргумент
имя конфигурационного файла.

Проверить работу функции на примере файла config_sw1.txt

Ограничение: Все задания надо выполнять используя только пройденные темы.
"""
'''
from pprint import pprint
    

def get_int_vlan_map(config_filename):
  with open('config_sw1.txt') as file:
    #pprint(get_int_vlan_map(file))   
    access_list = {} 
    trunk_list = {}
    intf = ''
    for line in config_filename:
        if 'interface' in line:
            intf = line.split()[-1]
        elif 'trunk allowed' in line:
            trunk_list[intf] = [int(v) for v in line.split()[-1].split(",")]#list(map(int, (line.split()[-1]).split(',')))
        elif 'access vlan' in line:
            access_list[intf] = int(line.split()[-1])
    print(trunk_list)
    #tup1 = (trunk_list, access_list)
    return access_list, trunk_list
'''
def get_int_vlan_map(config_filename):
    access_dict = {}
    trunk_dict = {}

    with open(config_filename) as cfg:
        for line in cfg:
            line = line.rstrip()
            if line.startswith("interface"):
                intf = line.split()[1]
            elif "access vlan" in line:
                access_dict[intf] = int(line.split()[-1])
            elif "trunk allowed" in line:
                trunk_dict[intf] = [int(v) for v in line.split()[-1].split(",")]
        return access_dict, trunk_dict
