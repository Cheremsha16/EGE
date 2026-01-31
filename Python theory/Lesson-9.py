# Цикл while

num = 0
while num < 5:
    #print("hello")
    num += 1

# Сумма цифр числа
num = 123
summ = 0
while num != 0:
    summ += num % 10
    num //= 10
#print(num, summ)


# Цикл for

#range(n, m, k) - формирует диапазон целых чисел от n до m не включительно с шагом k
# range(n) - диапазон от 0 до n не ) - формирует диапазон целых чисел от n до m не включительно с шагом 1

for i in range(2, -6, -1):
    print(i)
