with open(r"files/26-80.txt") as F:
    N = int(F.readline())
    data = {}
    for i in range(N):
        row, pos = map(int, F.readline().split())
        data[row] = data.get(row, []) + [pos]

mx_cnt, mx_row = -1, None
ttl_cnt = 0
for r in data:
    row = sorted(data[r])
    cnt = 0
    for i in range(len(row)):
        pos = row[i]
        if not (pos - 2 in row or pos - 1 in row or pos + 1 in row or pos + 2 in row):
            cnt += 1
            row += [pos + 2]
    if cnt > mx_cnt:
        mx_cnt = cnt
        mx_row = r
    ttl_cnt += cnt

print(ttl_cnt, mx_row)
