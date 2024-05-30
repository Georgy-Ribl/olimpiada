def f(n):
    s = bin(n).replace("0b", "")
    sm = sum(int(k) for k in s)
    if sm % 2 == 0:
        s += s[-2] + s[-1]
    else:
        s += s[-1] + s[-2]
    return int(s, 2)


for i in range(3, 1000):
    if f(i) >= 154:
        print(i)
        break
