'''
6 130
30 B
50 B
120 A
120 A
120 A
10 B
'''
with open(r'files/28.txt') as f:
    n, m = map(int, f.readline().split(' '))
    arr = []
    for i in range(n):
        price, tp = f.readline().strip().split()
        arr.append([int(price), tp])
    arr.sort()
    count_a, shopping_cart = 0, []
    for i in range(len(arr)):
        price, tp = arr[i]
        sm = sum(elem[0] for elem in shopping_cart)
        if m - sm - price >= 0:
            if tp == 'A':
                count_a += 1
            shopping_cart.append([price, tp])
            last_index = i
    shopping_cart.reverse()
    for price, tp in shopping_cart:
        if tp == 'B':
            tst = [price, tp]
            shopping_cart.remove(tst)
            sm = sum(elem[0] for elem in shopping_cart)
            for i in range(last_index, len(arr)):
                price, tp = arr[i]
                if tp == 'A' and m - sm - price >= 0:
                    count_a += 1
                    shopping_cart.append([price, tp])
                else:
                    shopping_cart.append(tst)
                    break
                last_index = i
            else:
                continue
            break
    print(count_a, m - sm)
