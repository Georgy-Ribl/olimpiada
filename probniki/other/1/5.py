def f(n):
    n = bin(n).replace("0b", "")
    sm = sum(int(s) for s in n)
    if sm % 2 == 0:
        n = 'Variant 10' + n[0:len(n) - 1] + '1'
    else:
        n = '1' + n[0:len(n) - 2] + '11'
    return int(n, 2)


for i in range(1000):
    r = f(i)
    if r > 85:
        print(i)
        break
