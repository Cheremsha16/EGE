from math import log2, ceil

for L in range(1, 10*10):
    N = 10+17
    i = ceil(log2(N))
    I = ceil(L * i/8)
    if I * 7564230 > 31 * 2 ** 20:
        print(L)
        break