import random
import array


def creat_matrix(a: int, b: int) -> list:
    arr = [[0 for s in range(b)] for _ in range(a)]
    for i in range(a):
        for j in range(b):
            arr[i][j] = random.randint(1, 1000)
    return arr
