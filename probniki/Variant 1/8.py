from other import defines
import itertools

alf = list(range(8))

arr = [list(s) for s in itertools.permutations(alf, 5)]
k = 0
for el in arr:
    # el = [7, 6, 5, 4, 3]
    # el = [0, 1, 2, 3, 4]
    r = el[0] != 0
    for i in range(4):
        if el[i] % 2 == el[i + 1] % 2:
            r = False
    if r:
        k += 1
print(k)

r = True
el = [0, 1, 2, 3, 4]
if el[0] != 0:
    for i in range(4):
        if (int(el[i]) % 2) == (int(el[i + 1]) % 2):
            r = False
print(r)
