s = input()

s = s.replace('. ', '#')
s = s.replace(', ', '. ')
s = s.replace('#', ', ')

ans = ''
i = 0
while i < len(s):
    r = ''
    if s[i] == ' ':
        if s[i + 1].islower():
            ans += s[i + 1].upper()
            i += 2
            continue
        else:
            ans += s[i + 1]
            ans += s[i + 2].upper()
            i += 3
            continue
    ans += s[i]
    i += 1
print(ans)
