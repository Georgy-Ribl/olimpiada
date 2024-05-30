from math import comb

with open(r'files/27_a.txt', 'r') as file:
    n, k = map(int, file.readline().split())
    arr = [int(file.readline()) for _ in range(n)]
ans = 0
prefix = [0]

# for i in range(n):
#
#     sm, sch = 0, 0
#     for j in range(i, n):
#         sm += arr[j]
#         sch += 1
#         if sm % 111 == 0 and sch >= k:
#             ans += 1
# print(ans)

ms = [[] for _ in range(111)]
ms[0].append(0)
for i in range(n):
    el = (prefix[-1] + arr[i]) % 111
    prefix.append(el)
    ms[el].append(i + 1)
for elem in ms:
    print(*elem)
for elem in ms:

# prefix[i] = (arr[0]+arr[1]+ .... + arr[i-1])%111
index = 0
print(prefix[index])
print(sum(arr[s] for s in range(index)) % 111)
