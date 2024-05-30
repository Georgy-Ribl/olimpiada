for A in range(10000, 1, -1):
    flag = True
    for x in range(1, 10000):
        for y in range(1, 10000):
            con = (x + y <= 25) or (x <= y + 5) or (x >= A)
            if not con:
                flag = False
                break
        if not flag:
            break
    if flag:
        print(A)
        break
