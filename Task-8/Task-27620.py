from itertools import product
ans=[]
alph=sorted('ИРСТУЦ')
for pos, val in enumerate(product(alph, repeat=5), start=1):
    val=''.join(val)
    if val[0] != '0' and val.count('И') ==2 and 'ЦЦ' not in val:
        ans.append(pos)
print(max(ans))  #7525