with open(r'files/24.txt') as f:
    s = f.read()
alf = 'ABCDEF1234567890'
ans = 0
k = 0
for i in range(len(s)):
    if s[i] in alf:
        k += 1
    else:
        ans = max(ans, k)
        k = 0
print(ans)
