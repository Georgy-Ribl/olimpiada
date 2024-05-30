from other.defines import conv


def f(n):
    ost = int(n) % 3
    n = conv(str(n), 10, 3)
    if ost == 0:
        n = '1' + n + '02'
    else:
        n = n + conv(str(ost * 4), 10, 3)
    return int(n, 3)


for i in range(1000, 0, -1):
    n = f(i)
    if n < 199:
        print(i)
        break
