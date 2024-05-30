for x in range(16):
    n = int('153' + str(x) + '4', 16) + int('1' + str(x) + '325', 16)
    if n % 15 == 0:
        print(n // 15)
        break
