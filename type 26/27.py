with open(r'files\27.txt', 'r') as f:
    n = int(f.readline())
    arr = []
    for i in range(n):
        rows = list(map(int, f.readline().split()))
        rows[1] = -rows[1]
        arr += [rows]
    arr.sort()
    r, m = 0, 0
    for i in range(1, len(arr)):
        for j in range(i + 1, len(arr)):
            if arr[i][0] == arr[j][0]:
                if arr[j][1] - arr[i][1] == 3:
                    r = arr[j][0]
                    m = -arr[j][1] + 1
            else:
                break
    print(r, m)
