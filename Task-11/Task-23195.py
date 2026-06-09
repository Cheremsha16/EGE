from math import log2, ceil

for N in range(1, 10**10):
    L =172
    i =ceil(log2(N))
    I =ceil(L*i/8)
    if I*356984 > 54 * 1024 *1024:
        print(N)
        break