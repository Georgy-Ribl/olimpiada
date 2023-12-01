from other import defines
import sys


def f(m, n):
    global arr
    if m == 1 and n == 1:
        return arr[1][1]
    if check[m][n] == 0:
        return max(f(m - 1, n) + arr[m][n], f(m, n - 1) + arr[m][n])
    else:
        return


m, n = map(int, input().split(" "))
arr = defines.creat_matrix(100, 100)
check = [[0 for _ in range(100)] for s in range(100)]
# for elem in arr:
#     print(*elem)
print(f(m, n))
