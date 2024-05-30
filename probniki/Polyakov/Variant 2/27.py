with open(r'files/27_a.txt') as f:
    n = int(f.readline())
    arr = [int(s) for s in f.readlines()]
dp = [arr[0] for _ in range(n)]
dp_index = [0 for _ in range(n)]
dp[1], dp[0] = arr[1], arr[0]
cursor = 0
for i in range(1, n):
    if dp[i - 1] > 0:
        dp[i] = arr[i] + dp[i - 1]
    else:
        dp[i] = arr[i]
        cursor = i
    dp_index[i] = cursor
ms = [0]
for i in range(dp_index[-1] - 1, -1, -1):
    if ms[- 1] > 0:
        ms.append(arr[i] + ms[- 1])
    else:
        ms.append(arr[i])

ans1 = ms[-1] + dp[-1]
ans2 = max(dp)
print(max(ans1, ans2))
