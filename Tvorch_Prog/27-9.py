with open("files/27-9b.txt") as f:
    n = int(f.readline())
    k = 6
    arr = [0] * k
    mn_odd = 1000
    mn_result = 1000000
    for i in range(n):
        if i >= k:
            if arr[i % k] % 2 == 1:
                mn_odd = min(mn_odd, arr[i % k])
        arr[i % k] = int(f.readline())
        if mn_odd != 1000 and arr[i % k] % 2 == 1:
            mn_result = min(mn_result, mn_odd * arr[i % k])

if mn_result == 1000000:
    print(-1)
else:
    print(mn_result)
