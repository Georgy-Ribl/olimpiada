from other import defines
from math import inf


def f(m, n):
    global matrix, dp
    mx = -inf
    for i in range(m):
        for j in range(n - 2, -1, -1):
            dp[i][j] = dp[i][j + 1] + matrix[i][j]
    return 0


m, n = map(int, input().split(' '))
dp = [[0 for _ in range(n)] for _ in range(m)]
matrix = defines.creat_matrix_not_abs(m, n)
for i in range(m):
    dp[i][n - 1] = matrix[i][n - 1]
mx = -inf
f(m, n)
for elem in dp:
    mx = max(max(elem), mx)

print(mx)
