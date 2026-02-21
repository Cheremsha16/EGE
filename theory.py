from math import log2, ceil

#1855
L = 101
N = 10 + 4090
i = ceil(log2(N))  #bit
I = ceil(L * i /8) # byte
print(I * 2048/1024)


#23270
for L in range(1, 10**6):
    N = 10 + 27
    i = ceil(log2(N))  #bit
    I = ceil(L * i /8) # byte
    if 3548 * I > 12 * 2 ** 10:
        print(L)
        break

#23195
for N in range(1, 10 ** 6):
    L = 172
    i = ceil(log2(N))  # bit
    I = ceil(L * i / 8)  # byte
    if 356984 * I >= 54 * 2 ** 20 :
        print(N)
        break