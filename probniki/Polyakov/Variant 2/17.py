with open(r'files/17.txt') as f:
    arr = [int(s) for s in f.readlines()]


def pr(x, y):
    x, y = str(x), str(y)
    if (len(x) == 2 and len(y) != 2) or (len(x) != 2 and len(y) == 2):
        return True
    return False


ans1, ans2 = 0, 10 ** 10
k = 0
for i in range(len(arr) - 1):
    if pr(arr[i], arr[i + 1]):
        k = max(k, arr[i] + arr[i + 1])
for i in range(len(arr)):
    if arr[i] > k:
        ans1 += 1
        ans2 = min(ans2, arr[i])
print(ans1, ans2)
