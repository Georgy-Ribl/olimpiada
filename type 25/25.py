from functools import wraps


@wraps(enumerate)
def F():
    for j in range(400000000, 600000000 + 1):
        i = j
        m = 0
        n = 0
        while i % 2 == 0:
            i //= 2
            m += 1
        if m % 2 == 0:
            while i % 3 == 0:
                i //= 3
                n += 1
        if n % 2 != 0 and i == 1:
            print(j)


F()
