from string import printable
from itertools import product 

cnt=0
for val in product(printable[:20], repeat=5):
    val=''.join(val)
    if val[0] != '0' and val(sum[0:6] == '26') and