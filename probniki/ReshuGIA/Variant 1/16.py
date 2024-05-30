from math import comb

sm = 0
for i in range(2, 31):
    sm += comb(i, 2)
print(sm)
