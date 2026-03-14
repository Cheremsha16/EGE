from itertools import product
from string import printable

for val in product(printable[:7], repeat=7):
    val=''.join(val)
    if val[0] != '0' and val. % 2 == 2:
        cnt +=  1
print(cnt)