with open(r'files/27_A.txt') as f:
    n = int(f.readline())
    arr = []
    for i in range(n):
        magaz, zakaz = map(int, f.readline().split())
        arr.append([magaz, zakaz // 45 + 1])
print(arr)
