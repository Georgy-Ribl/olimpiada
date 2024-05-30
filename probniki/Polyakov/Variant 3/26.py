with open(r'files/26.txt', 'r') as file:
    n, k = map(int, file.readline().split())
    arr = [list(map(int, file.readline().split())) for _ in range(n)]
arr.sort()
k, ls, emp, tmp = 0, 0, [0] * (k + 1), -1
for el in arr:
    tmp = -1
    for j in range(1, k + 1):
        if emp[j] <= el[0]:
            tmp = j
            break
        if tmp == -1:
            for l in range(1, k + 1):
                if emp[l] < el[1] and (tmp == -1 or emp[l] < emp[tmp]):
                    tmp = l
        if tmp != -1:
            k += 1
            ls = tmp
print(k, ls)
print()
