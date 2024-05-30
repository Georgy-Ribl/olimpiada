with open(r'files/36.txt', 'r') as f:
    n = int(f.readline())
    arr = sorted([int(f.readline()) for _ in range(n)], reverse=True)
arr_check = []
while len(arr) > 0:
    block = [arr.pop(0)]
    for i in range(len(arr)):
        if (block[-1] - arr[i]) >= 5:
            block.append(arr[i])
            arr[i] = ''
    arr = [x for x in arr if x != '']
    arr_check.append(block)
print(len(arr_check), max(len(c) for c in arr_check))
