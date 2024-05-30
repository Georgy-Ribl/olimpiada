with open(r'files/17.txt') as file:
    arr = [int(s) for s in file.read().split()]
k1 = min(s for s in arr if abs(s) % 10 == 4)
ans1, ans2 = 0, 0
for i in range(len(arr) - 1):
    a, b = arr[i], arr[i + 1]
    if (str(a)[-1] == '4' and str(b)[-1] != '4') or (str(b)[-1] == '4' and str(a)[-1] != '4'):
        if (a + b) ** 2 >= abs(k1):
            ans1 += 1
            ans2 = max(ans2, (a + b) ** 2)
print(ans1, ans2)
