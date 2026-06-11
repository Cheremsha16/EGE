from sys import setrecursionlimit

def G(n):
    if n < 10: return 2*n
    if n >= 10: return G(n-2)+1

def f(n):
    return 2*(G(n-3)+8)

setrecursionlimit(10000)
print(f(15548))