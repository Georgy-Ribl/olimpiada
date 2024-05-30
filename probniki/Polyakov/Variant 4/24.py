with open(r'files/24.txt') as f:
    s = f.read()
glas = 'AO'
sogl = 'BCD'
mx, k = 0, 1
for i in range(0, len(s) - 1, 2):
    if s[i] in glas and s[i + 1] in sogl:
        k += 1
    else:
        mx = max(mx, k)
        k = 1
print(mx)
