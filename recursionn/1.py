def f(n, dp):
    if dp[n] == -1:
        dp[n] = f(n - 1, dp) + f(n - 2, dp)
    return dp[n]


n = int(input())
dp = [-1 for _ in range(n)]
dp[0] = 0
dp[1] = 1
print(f(n - 1, dp))
a = 0
a1 = 1
for i in range(2, n):
    a, a1 = a1, a + a1
print(a1)

dp1 = [-1 for _ in range(n)]
dp1[0] = 0
dp1[1] = 1
for i in range(2, n):
    dp1[i] = dp1[i - 1] + dp1[i - 2]
print(dp1[-1])
