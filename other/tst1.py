import random


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

n = conv(str(8**740-2**900+7), 10, 2)
print(n.count('0'))
def rotate(matrix, k):
    # k столб -> k строка
    # k строка -> N - 1 - k столбец
    # N - 1 - k столбец -> N - 1 - k строка
    # N - 1 - k строка -> k столб
    N = len(matrix)
    a = min(k, N - 1 - k)
    b = max(k, N - 1 - k)
    for i in range(a, b):
        tmp = matrix[N - 1 - i][k]
        matrix[N - 1 - i][k] = matrix[N - 1 - k][N - 1 - i]  # N - 1 - k строка -> k столб --- ok
        matrix[N - 1 - k][N - 1 - i] = matrix[i][N - 1 - k]  # N - 1 - k столбец -> N - 1 - k строка -- ok
        matrix[i][N - 1 - k] = matrix[k][i]  # k строка -> N - 1 - k столбец -- ok
        matrix[k][i] = tmp  # k столб -> k строка

#
# matrix = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]
# print(*matrix, sep="\n")
# print()
# rotate(matrix, 2)
# print(*matrix, sep="\n")
#
#
#
#
#
# matrix = [[0] * 10 for i in range(10)]
# print(*matrix, sep = '\n')
# matrix[0][0] = 1
# print()
# print()
# print(*matrix, sep = '\n')
# a = [1, 2]
# b = a.copy()
# a.append(0)
# print(a, b)
#
# # matrix = список списков объектов
# # список = указатель на ячейку памяти, где он хранится
# # matrix = указатель на ячейку памяти, где хранится список указателей на ячейки памяти, где хранятся списки объектов
# # copy что делает - вместо копирования указателя создает новую область памяти, где хранится список, каждый элемент которого - копия каждого элемента изначального списка
# # = -- копирует указатель
# # matrix.copy() -- новая область памяти, где хранится список, каждый элемент которого - копия указателей на ячейки памяти, где хранятся списки объектов
#
# matrix1 = matrix.copy()
# matrix[0][0] = 15
# matrix.append([1] * 10)
# print()
# print()
# print(*matrix1, sep = '\n')
# print()
# print()
# print(*matrix, sep = '\n')
#
#
#
#
# def kol_symb(task):
#     k = 1
#     for elem in task:
#         if int(elem) == 0:
#             k += 1
#         else:
#             break
#     arr = []
#     # print(f"k = {k}")
#     for i in range(k, len(task) + 1):
#         if len(task) % i == 0:
#             arr.append(i)
#     return arr[0]
#
#
# letters = "abcdefghijklmnopqrstuvwxyz"
#
# task = input()
# sys, task = int(int(task) % 100), task[:len(task) - 2]
#
# n_symb = kol_symb(task)
#
# task_per_symb = []
# symbols_of_keyWord = ""
# k = 0
#
# for i in range(len(task)):
#     if k < n_symb:
#         symbols_of_keyWord += task[i]
#         k += 1
#     else:
#         task_per_symb.append(symbols_of_keyWord)
#         symbols_of_keyWord = task[i]
#         k = 1
#     if i == len(task) - 1:
#         task_per_symb.append(symbols_of_keyWord)
# answer = ""
# for elem in task_per_symb:
#     answer += letters[int(conv(elem, sys, 10)) - 1]
#
# print(answer.upper())
