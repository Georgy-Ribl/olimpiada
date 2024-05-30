with open(r'files/26_test.txt') as f:
    n = int(f.readline())
    arr = [list(map(int, f.readline().split())) for _ in range(n)]
arr.sort(key=lambda x: x[1], reverse=True)
arr.sort(key=lambda x: x[0], reverse=True)
print(arr)
ans1, ans2 = 0, 10 ** 10
k = 1
for i in range(n):
    k = 0
    ans1_moment, ans2_moment = 0, 10 ** 10
    for j in range(i, n):
        day, cash = arr[j][0], arr[j][1]
        if day - k >= 0:
            ans1_moment += cash
            ans2_moment = min(ans2_moment, cash)
        k += 1
    if ans1 < ans1_moment:
        ans1 = ans1_moment
        ans2 = ans2_moment
print(ans1, ans2)
