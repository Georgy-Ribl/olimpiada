with open(r'files/2.txt') as f:
    s, n = map(int, f.readline().split(' '))
    arr = []
    for i in range(n):
        arr.append(int(f.readline()))
    arr.sort()
    mx_n = 0
    sm = 0
    for i in range(n):
        if sm + arr[i] <= s:
            sm += arr[i]
            mx_n += 1
        else:
            break
    print(mx_n, end=' ')
    sm -= arr[mx_n - 1]
    mx_i = 0
    for i in range(mx_n - 1, len(arr)):
        if sm + arr[i] <= s:
            mx_i = arr[i]
    print(mx_i)
