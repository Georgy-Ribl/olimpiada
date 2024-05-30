def dpFunk(shift, arr):
    dp = []
    dp.append(arr[shift])
    dp.append(max(arr[shift], arr[shift + 1]))
    for i in range(shift + 2, len(arr) + shift - 1):
        dp.append(max(dp[-2] + arr[i], dp[-1]))
    return dp[-1]


with open(r'files/27_b.txt') as f:
    n = int(f.readline())
    arr = [int(f.readline()) for _ in range(n)]

print(max(dpFunk(0, arr), dpFunk(1, arr)))
