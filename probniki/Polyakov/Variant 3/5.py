for i in range(0, 1000):
    n = bin(i)[2:]
    if n.count('1') % 2 == 0:
        n = '1' + n + '00'
    else:
        n = '11' + n
    if int(n, 2) == 412:
        print(i)
        break
