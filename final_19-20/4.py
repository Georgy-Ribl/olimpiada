ip, n = map(str, input().split())
ip = [int(s) for s in ip.split('.')]
arr = []
ans = []
for i in range(int(n)):
    arr.append([s for s in input().split()])

for i in range(int(n)):
    ms1 = [int(s) for s in arr[i][0].split('.')]
    ms2 = [int(s) for s in arr[i][1].split('.')]
    for j in range(4):
        if ip[j] & ms2[j] != ms1[j] & ms2[j]:
            break
    else:
        ans.append([int(arr[i][2]), -i])
ans.sort(reverse=True)

if len(ans) > 0:
    print(-ans[0][1] + 1)
else:
    print(-1)
