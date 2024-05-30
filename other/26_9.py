with open(r'test.txt') as f:
    d, p = map(int, f.readline().split())
    arr = [[int(x) for x in s.split()] for s in f]
arr.sort()
print(arr)
ans1, ans2 = 0, 0
gorshochek = [0] * p
for elem in arr:

