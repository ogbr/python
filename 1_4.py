n = input("Введите целое положительное число")

# решение 1
max = 0
i = 0
while i < len(n):
    if int(n[i]) > max:
        max = int(n[i])
    i += 1
print(max)

# решение 2
max = 0
i = 0
n = int(n)
m=1
while m > 0:
    m = (n // (10 ** i)) % 10
    if max < m:
        max = m
    i += 1
print(max)
