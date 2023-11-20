def find_king(arr):
    kings = []
    for i in range(8):
        for j in range(8):
            if arr[i][j] == 'wK' or arr[i][j] == 'bK':
                kings.append([i, j, arr[i][j].strip('K')])
    return kings


def find_problems(pos_x, pos_y, color):
    global elem, n
    for x in range(8):
        for y in range(8):
            if elem[x][y] == colr.get(not color) + 'R' and (
                    (x != pos_x and y == pos_y) or (x == pos_x and y != pos_y)):
                print(n)
                exit()


def from_king(pos_x, pos_y, color):
    global elem, n
    for x in range(pos_x + 1, 8):
        if 'w' or 'b' in elem[x][pos_y]:
            if elem[x][pos_y] == colr.get(not color) + 'R':
                print(n)
            break


colr = {
    0: 'w',
    1: 'b'
}

arr = [[[str(s) for s in input().split()] for j in range(8)] for i in range(int(input()))]
n = 0
for elem in arr:
    n += 1
    pos_king = find_king(elem)
    for king in pos_king:
        if king[2] == 'w':
            king[2] = 0
        else:
            king[2] = 1
        find_problems(king[0] + 1, king[1], king[2])
        find_problems(king[0] + 1, king[1] + 1, king[2])
        find_problems(king[0] - 1, king[1], king[2])
        find_problems(king[0] - 1, king[1] - 1, king[2])
        find_problems(king[0] - 1, king[1] + 1, king[2])
        find_problems(king[0] + 1, king[1] - 1, king[2])
        find_problems(king[0], king[1] + 1, king[2])
        find_problems(king[0], king[1] - 1, king[2])

'''
wR 0 0 0  0 0 0 bK
 0 0 0 wR 0 0 0 0
 0 0 0 0  0 0 0 0
 0 0 0 0  0 0 0 0
 0 0 0 0  0 0 0 0
wK 0 0 0  0 0 0 0
 0 0 0 0  0 0 0 0
 0 0 0 0  0 0 0 0
'''
