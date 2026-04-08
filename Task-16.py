from functools import lru_cache

@lru_cache(None)
def G(n):
    if n<8: return 3*n
    if n >= 8: return G(n-3)+2
def F(n):
    return 3*(G(n-2)+5)

for i in range(1, 12350):
    F(i)
print(F(12345))