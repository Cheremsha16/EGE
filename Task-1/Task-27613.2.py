from itertools import permutations

graph='DB BE EF FA AD AC CE CB'.split()
matrix='36 456 145 236 23 124'.split()

print(*range(1, 6))
for i in permutations('ABCDEF'):
    if all(str(i.index(x)+1) in matrix[i.index(y)] for x, y in graph):
        print(*i)