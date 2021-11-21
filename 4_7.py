def fact(n):
    res = 1
    for i in range(1, n + 1):
        res *= i
        yield res


n = 4
for i, k in enumerate(fact(n)):
    if i < n:
        print(k)
