from math import ceil

with open(r'files\16.txt', 'r') as f:
    n = int(f.readline())
    ans = 0
    arr = []
    for i in range(n):
        p = int(f.readline())
        if p <= 50:
            ans += p
        else:
            arr.append(p)
    arr.sort()
    arr_to_sum = []
    to_discount = 0
    for i in range(len(arr)):
        if i < len(arr) // 2:
            to_discount += arr[i] * 0.75
            mx = arr[i]
        else:
            ans += arr[i]

    print(ans + ceil(to_discount), mx)
