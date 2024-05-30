import random

arr = [random.randint(-100, 100) for i in range(random.randint(10, 30))]
# arr = [-200, -50, 500, 100, -100]
k = random.randint(5, len(arr) - 5)

dp = [arr[0]]
for i in range(1, len(arr)):
    dp.append(max(0, dp[-1]) + arr[i])
pref = [0]
for i in range(len(arr)):
    pref.append(pref[-1] + arr[i])
maxx = -10 ** 9
for i in range(k, len(arr)):
    maxx = max(maxx, dp[i - k] + pref[i + 1] - pref[i + 1 - k])
print(maxx)
maxx_real = -10 ** 9
for i in range(len(arr) - k):
    s = 0
    for j in range(i, len(arr)):
        s += arr[j]
        if j - i >= k and s > maxx_real:
            maxx_real = s
print(maxx_real)
