import random


def creat_matrix(a: int, b: int) -> list[list]:
    matrix = [[0 for s in range(b)] for _ in range(a)]
    for i in range(a):
        for j in range(b):
            matrix[i][j] = random.randint(1, 10)
    return matrix
