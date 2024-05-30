with open(r'files/24.txt') as f:
    s = f.read()
ans = 0
k = 0

sogl = 'BCD'
glas = 'AE'

for i in range(0, len(s) - 1, 2):
    if s[i] in glas and s[i + 1] in sogl:
        k += 1
    else:
        ans = max(ans, k)
        k = 0
ans = max(ans, k)
for i in range(1, len(s) - 1, 2):
    if s[i] in glas and s[i + 1] in sogl:
        k += 1
    else:
        ans = max(ans, k)
        k = 0
ans = max(ans, k)
print(ans)
