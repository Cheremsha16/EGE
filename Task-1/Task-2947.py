from itertools import permutations

graph='ИГ ГБ БА АВ ВД ДЕ ЕИ ИЖ ЖД ЖГ БВ'.split()
matrix='267 157 468 356 248 134 12 35'.split()

print(*range(1, 8))
for i in permutations('АБВГДЕЖИ'):
    if all(str(i.index(x) + 1) in matrix [i.index(y)] for x, y in graph):
        print(*i) #39