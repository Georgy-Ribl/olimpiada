with open(r'files/34.txt', 'r') as f:
    n = int(f.readline())
    arr = [[0] * 10001 for i in range(10001)]
    for i in range(n):
        x, y = map(int, f.readline().split())
        arr[x][y] = 1
mx_len, mx = 0, 0
for i in range(1, 10001):
    k = 0
    for j in range(1, 10001):
        if j % 2 != 0:
            if arr[i][j] == 1 and arr[i][j + 1] == 0:
                k = k + 1
            else:
                if k > mx_len:
                    mx_len = k
                    mx = i
                k = 0
print(mx_len, mx)
