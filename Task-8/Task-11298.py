from itertools import product
ans=[]
alph = sorted('АЖЗОПЮ')
for pos, val in enumerate(product(alph, repeat=6), start=1):
    val = ''.join(val)
    if val // 2 == 0 and val[0] == 'А' and val.count('З') >= 2:
        ans.append(pos)
print(max(ans))