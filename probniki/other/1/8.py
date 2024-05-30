count = 0
for n in range(10000, 12000):
    r = oct(n).replace('0o', '0')
    r = r[1:len(r)]
    if r.count('2') == 2:
        for i in range(len(r)):
            if i == 0 and r[i] == '2':
                if r[i + 1] != 0:
                    count += 1

            elif i == len(r) - 1 and r[i] == '2':
                if r[i - 1] != '2':
                    count += 1

            elif r[i - 1] != '2' and r[i] == '2' and r[i + 1] != '2':
                count += 1

print(count)
