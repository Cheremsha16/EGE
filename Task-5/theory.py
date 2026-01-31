# Стандартные системы счисления
# Двоичная система
num=20
print(bin(num)[2:]) #str
print(f"{num:b}")
# Восьмеричная система
print(oct(num)[2:])
print(f"{num:0}")
# Шестнадцатеричная система
print(hex(num)[2:])
print(f"{num:x}")

# Перевод любую систему счисления (2 <= sys <= 9)
def convert(num, sys):
    res =''
    while num:
        res += str(num % sys)
        num //= sys
    return res[::-1]

print(convert(20,2))


# Перевод любую систему счисления (2 <= sys <= 36)
from string import printable

def convert(num, sys):
    res =''
    while num:
        res += printable[num % sys]
        num //= sys
    return res[::-1]

# Полезные алгоритмы
# Сумма цифр двоичной системы
num_bin =('10101')
print(num_bin.count('1'))
# Сумма цифр любой системы (2 <= sys <= 9)
print(sum(map(int, num_bin)))
# Сумма цифр любой системы (2 <= sys <= 36)
print(sum(map(lambda x: int (x, 36), num_bin)))