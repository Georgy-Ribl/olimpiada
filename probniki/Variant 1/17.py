with open(r'files/17.txt') as f:
    arr = list(map(int, f.readlines()))
    ans1, ans2 = 0, 0
    for i in range(0, len(arr) - 1):
        if arr[i] % 5 == 0 or arr[i + 1] % 5 == 0:
            if (arr[i] + arr[i + 1]) % 7 == 0:
                ans1 += 1
                ans2 = max(ans2, arr[i] + arr[i + 1])
    print(ans1, ans2)
