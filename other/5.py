def f(n):
    n = bin(n).replace("0b", "")
    for i in range(3):
        sum_0 = n.count("0")
        sum_1 = n.count("1")
        if sum_0 == sum_1:
            n += n[-1]
        else:
            n += "0" if sum_1 > sum_0 else "1"
    return int(n, 2)


for i in range(1, 1000000000):
    res = f(i)
    if res % 2 != 0 and res % 7 == 0:
        print(i)
