alf = {
    'start': 1,
    'end': -1
}

with open(r'files/26-128.txt') as f:
    n = int(f.readline())
    arr = []
    time_start = []
    i = 0
    for el in f:
        start, end = map(int, el.split())
        arr.append((start, alf['start'], i))
        time_start.append(start)
        arr.append((end, alf['end'], i))
        i += 1

arr.sort()
ans1, ans2, queue, trash = 0, 0, [], [0] * n
mx_rI = 0
for rI in range(len(arr)):
    time, flag, index = arr[rI]
    if flag == alf['start']:
        queue.append([time, flag, index])
    if flag == alf['end']:
        if trash[index] == 0:
            ans1 += 1
            ans2 = time
            for el in queue:
                trash[el[2]] = rI
            queue.clear()
            mx_rI = rI
for time, flag, index in arr:
    if flag == alf['end'] and trash[index] == mx_rI:
        ans2 = time
print(ans1, ans2)
