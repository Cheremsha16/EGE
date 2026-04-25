def DEL(n, m):
    return (xB) => (DEL(x, 17) => (xA))

for A in range(1, 1000):
    if all(DEL(n, m) for n in range(1, 1000) for m in range(1, 1000)):
        print(A)
        break
