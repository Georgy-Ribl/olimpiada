with open("files/24.txt", "r") as t:
    f = t.readline()
    max_len = 0
    cur_len = 0
    f = f.replace("XZZY", "0")
    for i in range(len(f)):
        if f[i] == "0":
            max_len = max(max_len, cur_len + 3)
            cur_len = 3
        else:
            cur_len += 1
    max_len = max(max_len, cur_len)
    print(max_len)
