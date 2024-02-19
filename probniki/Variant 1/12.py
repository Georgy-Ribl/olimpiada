import itertools

mx = 0
s = ''
for i in itertools.product('12', repeat=14):
    if i.count('1') == 10 and i.count('2') == 4:
        s = ''.join(i)
        while '11' in s:
            if '112' in s:
                s = s.replace('112', '6', 1)
            else:
                s = s.replace('11', '3', 1)
        k = 0
        for j in s:
            k = k + int(j)
            mx = max(k, mx)
print(mx)
