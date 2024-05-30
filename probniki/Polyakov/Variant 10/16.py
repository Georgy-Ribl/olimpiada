def f(n):
    if n < 9:
        return n // 3 + n % 3
    if n >= 9:
        return f(n // 9) + f(n % 9)


# k = 0
# for i in range(9):
#     res = f(i)
#     print(i, res)
#     if res == 33:
#         k += 1
# print(k)

# f(341278)
# f(3) + f(4) + f(1) + f(2) f(7) + f(8)
# 1+2+1+2+3+4 = 13

# 4*8+1*1 : 9*2
# 4*7+3+2 : 9*8*6
# 4*6+3*3 : 84*8
k1 = 9 * 2
k2 = 9 * 8 * 6
k3 = 84 * 8
print(k1 + k2 + k3)
# for x1 in range(9):
#     for x2 in range(9):
#         for x3 in range(9):
#             for x4 in range(9):
#                 for x5 in range(9):
#                     for x6 in range(9):
#                         for x7 in range(9):
#                             for x8 in range(9):
#                                 sm = (x1 + x2 + x3 + x4 + x5 + x6 + x7 + x8)
#                                 if sm == 31:
#                                     k += 1
# print(k)
