from itertools import product, permutations

def f(w, x , y, z):
    return (not z and y and x and not w) or (z and y and x and not w)

for i in product((0,1), repeat =7):
    table =[
        (i[0], 1, i[1], i[2]),
        (i[3], 0, 1, i[4]),
        (0, i[5], 0, i[6])
    ]
    if (len(set(table))) == len(table):
        for p in permutations('wxyz'):
            if all(f(**dict(zip(p, t))) == t[-1] for t in table):
                print(*p, sep='')