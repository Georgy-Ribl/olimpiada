with open(r'files/21.txt') as f:
    n, m = map(int, f.readline().split(' '))
    arr = []
    for i in range(n):
        price, k, tp = f.readline().strip().split()
        if tp == 'B':
            m -= int(price) * int(k)
        else:
            arr.append([int(price), int(k)])
    arr.sort()
    k_b = 0
    for price, k in arr:
        if price > m:
            break
        mult = min(k, m // price)
        k_b += mult
        m -= price * mult
    print(k_b, m)
