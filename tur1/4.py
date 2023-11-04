def get_diagonals(matrix):
    rows, cols = len(matrix), len(matrix[0])
    diagonals = []
    for d in range(rows - 1, -cols, -1):
        diagonal = [matrix[i][i + d] for i in range(rows) if 0 <= i + d < cols]
        if len(diagonal) >= 3:
            diagonals.append(diagonal)

    return diagonals


arr = [[int(s) for s in input().split()] for i in range(int(input()))]
n = len(arr)
diagonals = get_diagonals(arr)
correct_diagonals = []
for j in range(len(diagonals)):
    diag = sorted(diagonals[j])
    k = diag[1] - diag[0]
    for i in range(len(diag) - 1):
        if diag[i] + k != diag[i + 1]:
            break
    else:
        correct_diagonals.append(j)
        if len(correct_diagonals) == 2:
            print('Yes')
            for elem in correct_diagonals:
                print(*diagonals[elem])
            exit()
print('No')
