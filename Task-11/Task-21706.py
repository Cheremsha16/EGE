from math import log2, ceil
for N in range(1, 10**6):
    L = 119
    i = ceil(log2(N))
    I = ceil(L*i/8)
    if 125300*I>23 *2**20:
        print(N)
        break #4097
