s = '>' + '0' * 21
for i in range(1, 1000):
    n = s + '1' * i + '2' * 11
    while '>1' in n or '>2' in n or '>0' in n:
        n = n.replace('>1', '22>', 1)
        n = n.replace('>2', '2>', 1)
        n = n.replace('>0', '1>', 1)
    n = n.replace('>', '')
    sm = sum(int(k) for k in n)
    if sm % i == 0:
        print(i)
