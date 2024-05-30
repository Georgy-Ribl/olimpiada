from other import defines


def f(n):
    k = defines.conv(str(n), 10, 2)
    k = k[0:len(k) - 1]
    if n % 2 != 0:
        k += 'Variant 10'
    else:
        k += '01'
    k = defines.conv(k, 2, 10)
    return int(k)


for i in range(1000000):
    if f(i) == 2018:
        print(i)
        break
