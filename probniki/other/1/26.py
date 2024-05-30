with open(r'files/26.txt') as f:
    n = int(f.readline())
    arr = [int(f.readline()) for _ in range(n)]
skidka = {}

ans, k = 0, 0
for elem in arr:
    ans += elem
    if elem not in skidka:
        skidka[elem] = 1
    else:
        skidka[elem] += 1
    if skidka[elem] % 3 == 0:
        ans -= elem
        k += 1
print(ans, k)
