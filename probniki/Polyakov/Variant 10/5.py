def f(n):
    s = bin(n)[2:]
    return int(s[::-1] + s[-1], 2)


for i in range(1, 10000):
    n = f(i)
    if n > 99:
        print(i)
        break
