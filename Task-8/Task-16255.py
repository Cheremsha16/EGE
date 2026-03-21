from string import printable
from itertools import product

for val in product(printable[:9], repeat=7):
    val = ''.join(val)
    if val[0] != '0' and val.count('6') >= 1 and
