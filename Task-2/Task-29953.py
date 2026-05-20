from itertools import product, permutations

def f(w, x, y, z):
    return (not ((x <= w) <= (w == z))) and y

for i in product((0, 1), repeat=5):
    table= [
        (i[0], 0, 1, 0, 1),
        (0, i[1], i[2], 0, 1),
        (i[3], 1, 1, i[4], 1)
    ]
    if(len(set(table))) == len(table):
        for p in permutations('wxyz'):
            if all(f(**dict(zip(p, t))) == t[-1] for t in table):
                print(*p, sep='')