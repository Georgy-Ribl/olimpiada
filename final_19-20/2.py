arr = [[int(s) for s in input().split()] for i in range(int(input()))]
n = len(arr[0])
pos = [0, n - 1]
np = [1, 0]
check = [[False for k in range(n)] for i in range(n)]
ps = [[1, 0], [0, -1], [-1, 1]]
index = 0
check[pos[0]][pos[1]] = True
fib = [0, 1]
for k in range(n * (n + 1) // 2):
    if arr[pos[0]][pos[1]] == fib[-2]:
        fib.append(fib[-1] + fib[-2])
    if 0 <= pos[0] + np[0] <= n - 1 and 0 <= pos[1] + np[1] <= n - 1 and check[pos[0] + np[0]][pos[1] + np[1]] == False:
        pass
    else:
        index = (index + 1) % 3
        np = ps[index]
    pos[0] = pos[0] + np[0]
    pos[1] = pos[1] + np[1]
    check[pos[0]][pos[1]] = True

print(*fib[:-2])
