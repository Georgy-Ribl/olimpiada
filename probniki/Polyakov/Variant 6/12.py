def f(n):
    while '18' in n or '388' in n or '888' in n:
        n = n.replace('18', '8', 1)
        n = n.replace('388', '81', 1)
        n = n.replace('888', '3', 1)
    return n


for i in range(3, 10001):
    s = '1' + '8' * i
    res = f(s)
    if res.count('1') == 3:
        print(i)
        break
