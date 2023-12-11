from other import defines
import sys


def f(m, n):
    global matrix, check
    if check[m][n] == 0:
        if m == 0 and n == 0:
            check[m][n] = matrix[0][0]
        elif m == 0 and n >= 1:
            check[m][n] = f(m, n - 1) + matrix[0][n]
        elif m >= 1 and n == 0:
            check[m][n] = f(m - 1, n) + matrix[m][0]
        else:  # m>=1 and n>=1
            check[m][n] = max(f(m - 1, n) + matrix[m][n], f(m, n - 1) + matrix[m][n])
    return check[m][n]


m, n = map(int, input().split(" "))
matrix = defines.creat_matrix_abs(m, n)
check = [[0 for _ in range(n)] for s in range(m)]
# for elem in matrix:
#     print(*elem)
print(f(m - 1, n - 1))

check1 = [[0 for _ in range(n)] for s in range(m)]
check1[0][0] = matrix[0][0]
for i in range(1, m):
    check1[i][0] = check1[i - 1][0] + matrix[i][0]
for i in range(1, n):
    check1[0][i] = check1[0][i - 1] + matrix[0][i]
for i in range(1, m):
    for j in range(1, n):
        k = matrix[i][j]
        check1[i][j] = max(check1[i - 1][j] + k, check1[i][j - 1] + k)
print(check1[m - 1][n - 1])
# version 1
check1 = [0] * n
for i in range(m):
    temp = [0] * n
    temp[0] = matrix[i][0]
    for j in range(1, n):
        temp[j] = max(check1[j], temp[j - 1]) + matrix[i][j]
    check1 = temp
print(check1[n - 1])

# version 2
check1 = [0] * n
for i in range(m):
    check1[0] = matrix[i][0]
    for j in range(1, n):
        check1[j] = max(check1[j], check1[j - 1]) + matrix[i][j]
print(check1[n - 1])
