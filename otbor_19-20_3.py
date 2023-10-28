def move(l, idx, pos):
    new_idx = (idx + pos) % (len(l) - 1)
    el = l[idx]
    if new_idx > idx:
        for i in range(idx, new_idx):
            l[i] = l[i + 1]
    elif new_idx < idx:
        for i in range(idx, new_idx, -1):
            l[i] = l[i - 1]
    l[new_idx] = el
    return new_idx


s = list(input())
array = []
for i in range(len(s)):
    if not s[i].isdigit():
        array.append([s[i], 0])
    else:
        num = array[-1][1]
        num *= 10
        num += int(s[i])
        array[-1][1] = num

idx = 0
while idx < len(array):
    if array[idx][1] > 0:
        new_idx = move(array, idx, array[idx][1])
        array[new_idx][1] = 0
    if array[idx][1] == 0:
        idx += 1
for elem in array:
    print(elem[0], sep='', end='')
