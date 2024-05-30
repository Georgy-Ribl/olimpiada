def f(a, b):
    for i in range(2, min(a, b) + 1):
        if a % i == 0 and b % i == 0:
            return i
    return 'YES'


n, m = map(int, input().split())
print(f(n, m))
