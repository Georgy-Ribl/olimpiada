with open(r'files/20.txt') as f:
    n, m = map(int, f.readline().split(' '))
    arr = []
    print(n, m)
    for i in range(n):
        price, k, tp = f.readline().strip().split()
        if tp == 'A':
            m -= int(price) * int(k)
        else:
            arr.append([int(price), int(k)])
    arr.sort()
    print(m)
    print(arr)
    k_b = 0
    for price, k in arr:
        if price > m:
            break
        mult = min(k, m // price)
        k_b += mult
        m -= price * mult
    print(k_b, m)
