def f(n):
    k = []
    dl = 2
    while n != 1:
        if n % dl == 0:
            k.append(dl)
            n //= dl
        else:
            dl += 1
    return k


for i in range(10):
    for j in range(10):
        s = str(i) + '2' + str(j) + '2'
        prost = f(int(s))
        if len(prost) == 7:
            print(s, prost[-1])
