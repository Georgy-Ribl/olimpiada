with open(r'files/29.txt') as f:
    n, m = map(int, f.readline().split(' '))
    arr = []
    for i in range(n):
        price, tp = f.readline().strip().split()
        arr.append([int(price), tp])
    arr.sort()
    count_b = 0
    last_index = 0
    for i in range(len(arr)):
        price, tp = arr[i]
        if m - price >= 0:
            if tp == 'B':
                count_b += 1
            m -= price
        else:
            last_index = i
            break
    for i in range(last_index, len(arr)):
        price, tp = arr[i]
        if tp == "B":
            for last_index in range(last_index - 1, -1, -1):
                price_2, tp_2 = arr[last_index]
                if tp_2 == "A":
                    break
            else:
                break
            if m - price + price_2 >= 0:
                count_b += 1
                m = m - price + price_2
            else:
                break
    print(count_b, m)
