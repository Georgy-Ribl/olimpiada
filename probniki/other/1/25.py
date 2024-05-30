s = '1{}3124{}6'
count = 0
for i in range(10):
    for j in range(1000):
        n = int(s.format(i, j))
        if n % 1983 == 0:
            print(n, n // 1983)
            count += 1
        if count == 2:
            exit()
