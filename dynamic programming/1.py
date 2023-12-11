def f(houses) -> int:
    n = len(houses)
    if n == 0:
        return 0
    elif n == 1:
        return houses[0]

    mx = [0] * n
    mx[0] = houses[0]
    mx[1] = max(houses[0], houses[1])
    for i in range(2, n):
        sc = mx[i - 1]
        tc = mx[i - 2] + houses[i]
        mx[i] = max(sc, tc)
    return mx[-1]


houses = [6, 7, 1, 30, 8, 2, 4, 20, 3, 23, 24, 19, 9]
print(f(houses))
