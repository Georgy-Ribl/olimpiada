with open(r'files/18.txt') as f:
    n, m = map(int, f.readline().strip().split())
    arr = []
    k = 0
    pr = m
    for i in range(n):
        ch = int(f.readline().strip())
        if 200 <= ch <= 210:
            k += 1
            pr -= ch
        else:
            arr.append(int(ch))
    arr.sort()
    last_ind = -1
    for i in range(len(arr)):
        if pr - arr[i] >= 0:
            pr -= arr[i]
            k += 1
            last_ind = i
    if last_ind >= 0:
        mx = m
        pr += arr[last_ind]
        # 100 120 140 160 340
        for i in range(len(arr) - 1, -1, -1):
            if pr - arr[i] >= 0:
                pr -= arr[i]
                last_ind -= 1
                if last_ind < 0:
                    break
                pr += arr[last_ind]
    print(k, m - pr)
