def f(m, n):
    if m == 0 and n >= 1:
        return 1
    elif m >= 1 and n == 0:
        return 1
    elif m == 0 and n == 0:
        return 0
    return f(m - 1, n) + f(m, n - 1)


m, n = map(int, input().split(' '))
print(f(m, n))
