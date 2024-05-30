def f(d):
    if d[2] == [0]:
        return d[1]
    else:
        maxx = 0
        for i in d[2]:
            if maxx < f(index[i - 1]):
                maxx = f(index[i - 1])
        return maxx + d[1]


from csv import reader

with open(r"files/22.csv") as F:
    s = reader(F, delimiter=';', quotechar='"')
    next(s)
    index = []
    for i in s:
        index.append([int(i[0]), int(i[1]), list(map(int, str(i[2]).split(';')))])
    for i in range(len(index)):
        print(i + 1, f(index[i]))
