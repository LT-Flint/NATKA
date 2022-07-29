# -*- coding: utf-8 -*-
"""
Задание 12.1

Создать функцию ping_ip_addresses, которая проверяет пингуются ли IP-адреса.

Функция ожидает как аргумент список IP-адресов.

Функция должна возвращать кортеж с двумя списками:
* список доступных IP-адресов
* список недоступных IP-адресов

Для проверки доступности IP-адреса, используйте команду ping (запуск ping через subprocess).
IP-адрес считается доступным, если выполнение команды ping отработало с кодом 0 (returncode).
Нюансы: на Windows returncode может быть равен 0 не только, когда ping был успешен,
но для задания нужно проверять именно код. Это сделано для упрощения тестов.

Ограничение: Все задания надо выполнять используя только пройденные темы.
"""
import sys
import subprocess

ip_llist = ['8.8.8.8','8.8.8.1']

def ping_ip_addresses(ip_list):
    #result = {}
    right_ip = []
    unreach_ip = []
    for ip in ip_list:
        temp = subprocess.run(['ping' ,ip,'-c' , '2'], stdout=subprocess.DEVNULL, stderr=subprocess.PIPE)
        if not temp.returncode:
            right_ip.append(ip)
            #print(right_ip)
        else:
            unreach_ip.append(ip)
    result = [(right_ip,unreach_ip)]
    #print(right_ip)
    return right_ip, unreach_ip

if __name__ == '__main__':
    #subprocess.run(['ping', '-c', '3', '8.8.8.8'])
    #subprocess.run(['ping' ,'8.8.8.0','-c' , '2']
    print(ping_ip_addresses(ip_llist))
