def get_divisors(n):
    divisors = []
    sq = int(n ** 0.5)
    for i in range(2, sq):
        if n % i == 0:
            divisors.append(i)
            divisors.append(n // i)
    if sq ** 2 == n:
        divisors.append(sq)
    if len(divisors) < 5:
        return 0
    divisors.sort()
    ans = 1
    for elem in divisors[0:5]:
        ans *= elem
    return ans


n = 500_000_000
k = 0
for i in range(n + 1, n + 10000):
    if 0 < get_divisors(i) < i:
        print(get_divisors(i))
        k += 1
    if k == 5:
        exit()
