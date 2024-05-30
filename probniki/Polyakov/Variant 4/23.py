def f(x, y, k1):
    if x == 13:
        k1 = True
    if x == 23:
        return 0
    if x > y:
        return 0
    if x == y and k1 == True:
        return 1
    return f(x + 2, y, k1) + f(x * 3, y, k1) + f(x * 5, y, k1)


print(f(1, 75, False))
