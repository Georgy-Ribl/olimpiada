alf = {
    'start': 1,
    'end': -1,
}


def find_seat(end_time: int):
    global cotelki
    for rI in range(len(cotelki)):
        if rI == 0:
            if cotelki[rI] == -1 and cotelki[rI + 1] == -1:
                cotelki[rI] = end_time
                return rI
        elif rI == len(cotelki) - 1:
            if cotelki[rI] == -1 and cotelki[rI - 1] == -1:
                cotelki[rI] = end_time
                return rI
        elif cotelki[rI - 1] == -1 and cotelki[rI + 1] == -1 and cotelki[rI] == -1:
            cotelki[rI] = end_time
            return rI
    for rI in range(len(cotelki)):
        if cotelki[rI] == -1:
            cotelki[rI] = end_time
            if rI == 0:
                plohishi[rI] = False
                if cotelki[rI + 1] != -1:
                    plohishi[rI + 1] = False
            elif rI == len(cotelki) - 1:
                plohishi[rI] = False
                plohishi[rI - 1] = False
            else:
                plohishi[rI] = False
                if cotelki[rI - 1] != -1:
                    plohishi[rI - 1] = False
                if cotelki[rI + 1] != -1:
                    plohishi[rI + 1] = False
            return rI


with open(r'files/26-127.txt') as file:
    n = int(file.readline())
    arr = []
    for i in range(n):
        start = int(file.readline())
        end = start + 6
        arr.append([start, alf['start']])
        arr.append([end, alf['end']])
arr.sort()

trash = []
queue = []
ans1, ans2 = 0, 0
for time, flag in arr:
    if flag == alf['start']:
        queue.append([time, alf['start']])
    if flag == alf['end']:
        ans1 = max(ans1, len(queue))
        del queue[0]
plohishi = [True] * ans1
cotelki = [-1] * ans1
queue.clear()
for time, flag in arr:
    if flag == alf['start']:
        queue.append([time, alf['start']])
        find_seat(time + 6)
    if flag == alf['end']:
        for rJ in range(len(cotelki)):
            elem = cotelki[rJ]
            if elem == time:
                cotelki[rJ] = -1
                if plohishi[rJ]:
                    ans2 += 1
                plohishi[rJ] = True
        ans1 = max(ans1, len(queue))
        del queue[0]

print(ans1, ans2)
