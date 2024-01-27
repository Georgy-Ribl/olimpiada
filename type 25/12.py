dip = [2422000, 2422081]


def count_d(n):
    k = 0
    for i in range(1, int(n ** 0.5) + 1):
        if n % i == 0:
            k += 1
        if k > 1:
            return 0
    if k == 1:
        return 1
    else:
        return 0


k = 1
for i in range(dip[0], dip[1]):
    if count_d(i) == 1:
        print(k, i)
        k += 1
