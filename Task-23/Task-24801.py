def f(x, y):
    if x == y: return 1
    if x > y: return 0
    return f(x + 1, y) + f(x + 2, y) + f(x +4, y) + f(x + 8, y)
print(f(16, {24:33}) * f({24:33}, 48))