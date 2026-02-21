ans = []
for N in range(1, 100_000):
    R = f'{N:b}'
    if R.count('1')%2==0:
        R='1'+R[2:]+'00'
    else:
        R='11'+R[2:]+'1'

        ans.append(R)
print(min(ans))