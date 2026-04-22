from itertools import combinations

def f(x):
    P = 15 <= x <= 142
    Q = 38 <= x <= 167
    A = A1 <= x <= A2
    return not (Q <= (not A and P)) <= (not Q)

line_A = [15, 38, 142, 167]
line_X = [15.5, 38.5, 142.5, 167.5]

ans=[]
for A1, A2 in combinations(line_A, 2):
    if all(not f(x) for x in line_X):
       ans.append(A2-A1)
print(min(ans)) #104