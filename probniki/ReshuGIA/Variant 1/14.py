s = 49 ** 7 + 7 ** 20 - 28
ans = ''
while s > 0:
    ans += str(s % 7)
    s //= 7
print(ans.count('6'))
