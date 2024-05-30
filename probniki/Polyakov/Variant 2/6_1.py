for x in range(10000, 1, -1):
    con = (3 * x - 1) ** 2 - (x + 1) ** 2
    if con <= 1000000:
        print(x)
        break
