alf = {
    'start': 1,
    'end': -1
}
with open(r'files/26-147.txt') as f:
    n = int(f.readline())
    arr = []
    for i in range(n):
        time, end = map(int, f.readline().split())
        end = time + end
        arr.append([time, alf['start'], i])
        arr.append([end, alf['end'], i])
arr.sort()
# print(arr)
ans1, ans2 = 0, 1
zanatost = []
for time, flag, index in arr:
    if flag == alf['start']:
        r = True
        for i in range(len(zanatost)):
            if zanatost[i] == -1:
                zanatost[i] = index
                r = False
                if i == 0:
                    ans2 += 1
                break
        if r:
            zanatost.append(index)
        # print(zanatost)
    if flag == alf['end']:
        for i in range(len(zanatost)):
            if zanatost[i] == index:
                zanatost[i] = -1
print(len(zanatost), ans2)
