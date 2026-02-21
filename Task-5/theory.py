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

# Перевод в 10 систему
# int(num, sys), где sys - система ИЗ КОТОРОЙ ПЕРЕВОДИМ

# Перевод любую систему счисления (2 <= sys <= 9)
def convert(num, sys):
    res =''
    while num:
        res += str(num % sys)
        num //= sys
    return res[::-1] if res else '0'

print(convert(20,2))


# Перевод любую систему счисления (2 <= sys <= 36)
from string import printable

def convert(num, sys):
    res =''
    while num:
        res += printable[num % sys]
        num //= sys
    return res[::-1] if res else '0'

# Полезные алгоритмы
# Сумма цифр двоичной системы
num_bin =('10101')
print(num_bin.count('1'))
# Сумма цифр любой системы (2 <= sys <= 9)
print(sum(map(int, num_bin)))
# Сумма цифр любой системы (2 <= sys <= 36)
print(sum(map(lambda x: int (x, 36), num_bin)))

# Замена символов в строке
# Заменить N символов слева - R[N:]
# Заменить N символов справа - R[:-N]
# Заменить ВСЕ символы в строке (все 0 поменять на 1)
R = '1010'
R = R.replace('0', '1')

# Заменить ВСЕ символы в строке (все 1 поменять на 3, 3 поменять на 1)
R = R.replace('1', '*')
R = R.replace('3', '1')
R = R.replace('*', '3')

# Усложнённые варианты вопросов
# Максимальное N при максимальном R
ans.append([R, N])
print(max(ans))
# Минимальное N при минимальном R
ans.append([R, N])
print(min(ans))
# Минимальное N при максимальном R
ans.apanspend([R, N])
ans = sorted(ans, key=lambda x:(-x[0], x[1]))
print(ans[0])
# Максимальное N при минимальном R
ans.apanspend([R, N])
ans = sorted(ans, key=lambda x:(x[0], -x[1]))
print(ans[0])



