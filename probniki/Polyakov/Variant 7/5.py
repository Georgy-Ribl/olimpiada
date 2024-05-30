def f(n):
    n = bin(n).replace("0b", "")
    if n.count("1") > n.count("0"):
        n = n + '0'
    else:
        n = n + '11'
    return int(n, 2)


for i in range(10000):
    if f(i) > 2019:
        print(i)
        break
