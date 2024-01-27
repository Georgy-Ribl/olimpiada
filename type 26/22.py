with open(r'files\22.txt', 'r') as f:
    n = int(f.readline())
    arr_to_check = []
    arr = []
    k = 0
    mx = -1 * 10 ** 10
    for i in range(n):
        x = int(f.readline())
        if x % 2 == 0:
            arr_to_check.append(x)
        arr.append(x)
    arr = set(arr)
    for i in range(len(arr_to_check)):
        for j in range(i + 1, len(arr_to_check)):
            srarf = (arr_to_check[i] + arr_to_check[j]) // 2
            if srarf in arr:
                k += 1
                mx = max(mx, srarf)
    print(k, mx)
