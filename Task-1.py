from itertools import permutations

graph='GE EF FA AB BG BC CE CD DF DA'.split()
matrix='457 567 45 136 123 247 126'.split()

print(*range(1,7))
for i in permutations('ABCDEFG'):
    if all(str(i.index(x)+1) in matrix[i.index(y)] for x, y in graph):
        print(*i)