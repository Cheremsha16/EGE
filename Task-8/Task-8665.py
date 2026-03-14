from string import printable
from itertools import product

cnt=0
for val in product(printable[:12], repeat=7):
    val = ''.join(val)
    if val[0] != '0' and val.count('B') == 2

        cnt += 1