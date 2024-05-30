from other.defines import conv

ans = 1
for x in range(17):
    for y in range(17):
        r1 = int('5' + conv(str(x), 10, 22) + conv(str(x), 10, 22) + '78', 17)
        r2 = int('4' + conv(str(x), 10, 22) + conv(str(x), 10, 22) + '9', 18)
        r3 = int('88' + conv(str(x), 10, 22) + conv(str(x), 10, 22) + '5', 19)
        r4 = int('6' + conv(str(x), 10, 22) + conv(str(y), 10, 22) + '23', 22)
        n = r1 + r2 + r3 - r4
        if n > 0 and n % 405 == 0:
            ans *= x
            ans *= y
print(ans)
