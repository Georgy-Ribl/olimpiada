N, M = map(int, input().split())
matr = []
for i in range(N):
    matr.append(list(map(int, input().split())))
dp = [[[0] * 3 for j in range(M + 1)] for i in range(N + 1)]
best_res = -float("inf")
best_pair = None
for i in range(N - 1, -1, -1):
    for j in range(M - 1, -1, -1):
        dp[i][j][0] = dp[i + 1][j][1] + matr[i][j]
        dp[i][j][1] = dp[i][j + 1][2] + matr[i][j]
        dp[i][j][2] = dp[i + 1][j][0] + matr[i][j]
        if dp[i][j][0] > best_res:
            best_pair = (i + 1, j + 1)
            best_res = dp[i][j][0]
print(best_res)
print(*best_pair)
