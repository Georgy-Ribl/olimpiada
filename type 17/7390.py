with open(r'files/17-399.txt') as f:
    arr = [int(s) for s in f.readlines()]


def if_four(arr):
    flag = ''
    for elem in arr:
        if abs(elem) % 10 == 4:
            flag += '1'
        else:
            flag += '0'
    if flag.count('1') == 1:
        return True
    return False


k1 = min(s for s in arr if len(str(abs(s))) == 3 and str(abs(s))[0] == '5')
ans1, ans2 = 0, 0

for i in range(len(arr) - 1):
    a, b = arr[i], arr[i + 1]
    sm = a + b
    if if_four([a, b]) and sm % k1 != 0:
        ans1 += 1
        ans2 = max(ans2, sm)
print(ans1, ans2)
