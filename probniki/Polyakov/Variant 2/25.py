def f(n):
    global alf
    n = str(n)
    if n not in alf:
        alf.append(n)
    while len(n) < 2:
        n = '0' + n
        if n not in alf:
            alf.append(n)
    return n


alf = []
for i in range(10000):
    alf.append(f(i))
s = '1*2??76'
k = s
arr_ans = []
for x in alf:
    k = k.replace('*', x, 1)
    for i in range(10):
        k = k.replace('?', str(i), 1)
        for j in range(10):
            if int(k.replace('?', str(j), 1)) % 1923 == 0:
                arr_ans.append([k.replace('?', str(j), 1), int(k.replace('?', str(j), 1)) // 1923])
        k = s
        k = k.replace('*', x, 1)
arr_ans = sorted(arr_ans)
for elem in arr_ans:
    print(elem[0], elem[1])
