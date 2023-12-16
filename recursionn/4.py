from other import defines
from math import inf

N, M = map(int, input().split())
matr = defines.creat_matrix_not_abs(N, M)
for elem in matr:
    print(*elem)
dp = [[[0] * 2 for j in range(M + 1)] for i in range(N + 1)]
best_res = -inf
best_pair = None
for i in range(N - 1, -1, -1):
    for j in range(M - 1, -1, -1):
        dp[i][j][0] = dp[i + 1][j][1] + matr[i][j]
        dp[i][j][1] = dp[i][j + 1][0] + matr[i][j]
        if dp[i][j][0] > best_res:
            best_pair = (i + 1, j + 1)
            best_res = dp[i][j][0]
print(best_res)
print(*best_pair)
