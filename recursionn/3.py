from other import defines
import sys


def f(m, n):
    global arr
    if check[m][n] == 0:
        if m == 0 and n == 0:
            check[m][n] = arr[0][0]
        elif m == 0 and n != 0:
            check[m][n] = arr[0][n]
        elif n != 0 and n == 0:
            check[m][n] = arr[m][0]
        else:
            if m > 1 and n > 1:
                check[m][n] = max(f(m - 1, n) + arr[m][n], f(m, n - 1) + arr[m][n])
            else:
                if m == 0 and n != 0:
                    check[0][n] = arr[0][n]
                elif n != 0 and n == 0:
                    check[m][0] = arr[m][0]
        return check[m][n]


m, n = map(int, input().split(" "))
arr = defines.creat_matrix(100, 100)
check = [[0 for _ in range(100)] for s in range(100)]
print(f(m, n))
