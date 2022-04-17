# -*- coding: utf-8 -*-
"""
Задание 6.2a

Сделать копию скрипта задания 6.2.

Добавить проверку введенного IP-адреса.
Адрес считается корректно заданным, если он:
   - состоит из 4 чисел (а не букв или других символов)
   - числа разделенны точкой
   - каждое число в диапазоне от 0 до 255

Если адрес задан неправильно, выводить сообщение: 'Неправильный IP-адрес'

Сообщение "Неправильный IP-адрес" должно выводиться только один раз,
даже если несколько пунктов выше не выполнены.

Ограничение: Все задания надо выполнять используя только пройденные темы.
"""
ip_in = input('Insert ip add: ')
buf = ip_in.split('.')

flag = True

for a in buf:
        if a.isdigit() and ip_in.count('.') == 3 and (int(a) >= 0 and int(a) < 256):
            pass
        else:
            #print("Неправильный IP-адрес")
            flag = False
            break
            
            #raise ValueError('Неправильный IP-адрес')
if flag:
  if ip_in == '0.0.0.0':
    print('unassigned')
  elif ip_in == '255.255.255.255':
    print('local broadcast')
  elif int(buf[0]) >= 1 and int(buf[0]) <= 223:
    print('unicast')
  elif int(buf[0]) > 223 and int(buf[0]) <= 239:
    print('multicast')
  else:
    print('unused')
else:
  print("Неправильный IP-адрес")
