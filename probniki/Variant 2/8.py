al = 'МАТВЕЙ'
k = 0
for b1 in 'МАТВЕ':
    for b2 in al:
        for b3 in al:
            for b4 in al:
                for b5 in al:
                    for b6 in al:
                        s = b1 + b2 + b3 + b4 + b5 + b6
                        bb = set(s)
                        if len(s) == len(bb) and s.count('АЕ') == 0:
                            k += 1
print(k)
