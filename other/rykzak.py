for x1 in range(2):
    for x2 in range(2):
        for x3 in range(2):
            for x4 in range(2):
                con1 = x1 and x3 and not x4
                con2 = not x3 and not x1 and not x2
                con3 = not (con1 or not x2 or con2)
                con4 = x2 and x4 and x1
                con5 = con4 or not x4 or con3
                con6 = not (con5 and con3)
                if con6 != True:
                    con6 = 0
                else:
                    con6 = 1
                print(con6, end='')

print()
print('1 1 0')
for A in range(1,10):
    for B in range(1,10):
        for C in range(1,10):
            if A % 2 == 0:
                a = 0
            else:
                a = 1
            if B % 2 == 0:
                b = 0
            else:
                b = 1
            if C % 2 == 0:
                c = 0
            else:
                c = 1
            F = (not a + (not b)) and not(not b + (not c))
            if F == 1:
                print(A,B,C)
            break


print([conv(str(s), 10, 2) for s in range(1, 16)])

