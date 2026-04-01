def f(x, y):
    if x == y: return 1
    if x > y or x==18 or x ==30: return 0
    return f(x+1, y)+ f(x*3, y)+ f(x*5, y)
print(f(2, 90))