mx = 0
for A in range(0, 10000):
    A_end = A + 1
    for x in range(1, 10000):
        con = (not ((369 <= x <= 3894) <= ((1381 <= x <= 2165) or (2643 <= x <= 3155))) <= (
            not (A <= x <= A_end) <= (369 <= x <= 3894)))
        A_end += 1
        if con == 0:
            A_end = x
    mx = max(mx, A_end - A + 1)
print(mx)
