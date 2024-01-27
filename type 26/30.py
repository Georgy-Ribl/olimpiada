with open(r'files/30.txt') as f:
    n = int(f.readline())
    s, e = 1633046400, 1633046400 + 31 * 24 * 60 * 60
    p = [0] * (e - s + 1)
    for _ in range(n):
        a, b = map(int, f.readline().split())
        a = max(a, s)
        if b == 0:
            p[a - s] += 1
        else:
            p[a - s] += 1
            p[b - s] -= 1
    for i in range(1, len(p)):
        p[i] += p[i - 1]
    x, y = 1633305600, 1633305600 + 7 * 24 * 60 * 60
    m, t = 0, 0
    for i in range(x - s, y - s):
        if p[i] > m:
            m, t = p[i], 0
        if p[i] == m:
            t += 1
    print(m, t)
