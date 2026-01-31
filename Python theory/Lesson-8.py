# Подключение дополнительных модулей / библиотек

# # Стандартный вызов библиотеки
# import math
# print(math.sqrt(9))
#
# # Вызов библиотеки через псевдоним
# import math as m
# print(m.sqrt(9))
#
# # Подключение одной команды из библиотеки
# from math import sqrt
# print(sqrt(9))
#
# # Подключение одной команды из библиотеки через псевдоним
# from math import sqrt as s
# print(s(9))
#
# # Подключение нескольких команды из библиотеки через псевдоним
# from math import sqrt as s, log2 as l
# print(s(9))

# Полезные функции из math
#Подключение всех команд из библиотеки
from math import *

print(ceil(4.1))# округление вверх
print(floor(4.9))# округление вниз
print(sqrt(4))# квадратный корень
print(log(8, 2))
print(pi, e)# константы
