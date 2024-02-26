with open(r'files/33.txt') as f:
    n = int(f.readline())
    a = [[0] * 10001 for j in range(10001)]
    for i in range(n):
        x, y = map(int, f.readline().split())
        a[x][y] = 1
mx, mn = 0, 0
for i in range(10001):
    k, ans = 0, 0
    for j in range(10001):
        if a[i][j] == 1:
            k += 1
            ans = max(k, ans)
        else:
            k = 0
    if ans > mx:
        mx = max(mx, ans)
        mn = i
print(mx, mn)
