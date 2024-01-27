s = '12345?7?8'

for i in range(10):
    for j in range(10):
        rt = s
        rt = rt.replace('?', str(i), 1)
        rt = rt.replace('?', str(j), 1)
        if int(rt) <= 10 ** 9 and int(rt) % 23 == 0:
            print(int(rt), int(rt) // 23)
