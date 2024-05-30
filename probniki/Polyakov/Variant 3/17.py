with open(r'files/17.txt') as f:
    arr = [int(s) for s in f.readlines()]

k1 = max(s for s in arr if len(str(s)) == 2)
ans1, ans2 = 0, 0
for i in range(len(arr) - 1):
    if len(str(arr[i])) == 2 or len(str(arr[i + 1])) == 2:
        if arr[i] + arr[i + 1] <= k1:
            ans1 += 1
            ans2 = max(ans2, arr[i] + arr[i + 1])
print(ans1, ans2)
