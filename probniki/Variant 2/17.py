with open(r'files/17.txt') as f:
    arr = [int(i) for i in f]
    k1 = [int(x) for x in arr if int(x) % 2 == 0]
    k1 = sum(k1) / len(k1)
    ans1, ans2 = 0, 0
    for j in range(0, len(arr) - 1):
        if ((arr[j] % 3 == 0) or (arr[j + 1] % 3 == 0)) and ((arr[j] < k1) or (arr[j + 1] < k1)):
            ans1 += 1
            ans2 = max(ans2, arr[j] + arr[j + 1])
print(ans1, ans2)
