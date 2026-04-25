def f(x, y):
    return (2*x + 3*x != 135) or (y>A) or (x>A)

for A in range(0,1000):
    if all(f(x, y) for x in range(0, 1000) for y in range(0, 1000)):
        print(A) #26