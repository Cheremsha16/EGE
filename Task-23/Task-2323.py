def f(x, y):
    if x == y: return 1
    if x > y: return 0
    num=str(x)
    if num[1] <num[2]:
        reverse_x = int(num[0]+ num[2]+ num[1])
        return f(x+1, y)+ f(reverse_x, y)
    else:
        return f(x+1, y)
print(f(101, 154))