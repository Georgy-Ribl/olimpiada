with open(r'files/17-390.txt') as file:
    arr = [int(s) for s in file.readlines()]


def f1(elems):
    k1 = sum(1 for s in elems if len(str(abs(s))) == 4)
    if 0 < k1 < 3:
        return True
    return False


def f2(elems):
    k_13 = sum(1 for s in elems if abs(s) % 13 == 0)
    k_7 = sum(1 for s in elems if abs(s) % 7 == 0)
    if k_13 > k_7:
        return True
    return False


def f3(elems):
    global sr
    for elem in elems:
        if elem < sr:
            return False
    return True


sr, k = 0, 0
for elem in arr:
    if abs(elem) % 1000 == 151:
        k += 1
        sr += elem
sr = sr / k
ans1, ans2 = 0, 10 ** 10
for i in range(len(arr) - 2):
    three_elems = [arr[i], arr[i + 1], arr[i + 2]]
    if f1(three_elems) and f2(three_elems) and f3(three_elems):
        ans1 += 1
        ans2 = min(ans2, sum(three_elems))
print(ans1, ans2)
