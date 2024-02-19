with open(r'files/33.txt') as f:
    n = int(f.readline())
    arr = [[int(s) for s in f.readline().split()] for _ in range(n)]
    print(arr)
