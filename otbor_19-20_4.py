def f4(x: int, y: int, l: int) -> int:
    global longest, board, m, n
    if x < n - 1 and board[x][y] == board[x + 1][y] - 1:
        f4(x + 1, y, l + 1)
    if x > 0 and board[x][y] == board[x - 1][y] - 1:
        f4(x - 1, y, l + 1)
    if y < m - 1 and board[x][y] == board[x][y + 1] - 1:
        f4(x, y + 1, l + 1)
    if y > 0 and board[x][y] == board[x][y - 1] - 1:
        f4(x, y - 1, l + 1)
    if l > longest:
        longest = l


board, longest = [], 0
n, m = map(int, input().split())
for i in range(n):
    board.append(list(map(int, input().split())))
for i in range(n):
    for j in range(m):
        f4(i, j, 1)
print(longest)
