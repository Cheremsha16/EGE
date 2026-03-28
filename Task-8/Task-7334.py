from itertools import product
ans=[]
alph = sorted('МЫСЛЬ')
for pos, val in enumerate(product(alph, repeat=5), start=1):
    val=''.join(val)
    if val[0] != '0' and val[0] == 'ЫЫ':
        ans.append(pos)
print(ans)