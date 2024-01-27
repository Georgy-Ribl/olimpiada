def get_divisors(n):
    divisors = []
    sq = int(n ** 0.5)
    for i in range(2, sq):
        if n % i == 0:
            divisors.append(i)
            divisors.append(n // i)
    if sq ** 2 == n:
        divisors.append(sq)
    if len(divisors) < 2:
        return 0
    divisors.sort()
    return divisors[-1] + divisors[0]


n = 700_000
k = 0
for i in range(n + 1, n + 10000):
    M = get_divisors(i)
    if M % 10 == 8:
        k += 1
        print(i, M)
    if k == 5:
        exit()
