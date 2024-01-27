from functools import lru_cache


@lru_cache()
def F(x, p):
    if 36 <= x and x <= 60 or p > 3:
        return p == 3
    if x > 60:
        return p % 2 == 1

    if p % 2 == 0:
        return F(x + 1, p + 1) and F(x * 2, p + 1) and F(x * 3, p + 1)
    else:
        return F(x + 1, p + 1) or F(x * 2, p + 1) or F(x * 3, p + 1)

# for i in range(1, 36):
#     if F(i, 1):
#         print(i)
