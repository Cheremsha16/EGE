from itertools import product
ans=[]
alph=sorted('БМНРЮ')
for pos, val in enumerate(product(alph, repeat=6), start=1):
    val=''.join(val)
    if val[0] != 'М' and val.count('Р') >= 2 and val != 'Ю':
        ans.append(pos)
print(max(ans))

