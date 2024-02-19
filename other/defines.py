import random


def creat_matrix_abs(a: int, b: int) -> list[list]:
    matrix = [[0 for s in range(b)] for _ in range(a)]
    for i in range(a):
        for j in range(b):
            matrix[i][j] = random.randint(1, 10)
    return matrix


def creat_matrix_not_abs(a: int, b: int) -> list[list]:
    matrix = [[0 for s in range(b)] for _ in range(a)]
    for i in range(a):
        for j in range(b):
            matrix[i][j] = random.randint(-10, 10)
    return matrix


def conv(n: str, ri: int, ro: int) -> str:
    digs = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    acc: int = 0
    for a in n:
        kl = digs.find(a)
        acc = acc * ri + kl
    res = ""
    while (acc > 0):
        kl = acc % ro
        res = digs[kl] + res
        acc = acc // ro
    return res
