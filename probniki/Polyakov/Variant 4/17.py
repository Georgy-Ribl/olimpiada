def f_k2(a, b):
    k = 0
    if len(str(a)) == 3:
        k += 1
    if len(str(b)) == 3:
        k += 1
    return k


with open(r'files/17.txt') as f:
    arr = list(int(s) for s in f.readlines())
k1 = min(s for s in arr if s % 100 == 11 and len(str(s)) == 3)
ans1, ans2 = 0, 0
for i in range(len(arr) - 1):
    k2 = f_k2(arr[i], arr[i + 1])
    if k2 == 1:
        if abs(arr[i] - arr[i + 1]) % k1 == 0:
            ans1 += 1
            ans2 = max(ans2, arr[i] + arr[i + 1])
print(ans1, ans2)
