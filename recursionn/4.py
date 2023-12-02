def f(m, n):
    if m == 0 or n == 0:
        return 1
    return f(m - 1, n) + f(m, n - 1)


m, n = map(int, input().split(' '))
print(f(m, n))
