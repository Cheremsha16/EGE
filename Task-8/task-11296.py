from itertools import product
alph = sorted('ДОСЖ')
ans=[]
for pos, val in enumerate(product(alph, repeat=6), start=1):
    val = ''.join(val)
    if val[0] == 'ЖС':
        ans.append(pos)
print(max(ans))