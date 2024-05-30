'''
6 130
30 B
50 B
120 A
120 A
120 A
Variant 10 B
'''
with open(r'files/28.txt') as f:
    n, m = map(int, f.readline().split(' '))
    arr = []
    for i in range(n):
        price, tp = f.readline().strip().split()
        arr.append([int(price), tp])
    arr.sort()
    count_a = 0
    last_index = 0  # указывает на индекс последнего взятого элемента + 1
    for i in range(len(arr)):
        price, tp = arr[i]
        if m - price >= 0:
            if tp == 'A':
                count_a += 1
            m -= price
        else:
            last_index = i
            break
    for i in range(last_index, len(arr)):  # перебираем все элементы, которые не вошли в изначальный набор
        price, tp = arr[i]
        if tp == "A":  # новый элемент это А
            for last_index in range(last_index - 1, -1, -1):  # перебираем элементы из начального набора в поисках В
                price_2, tp_2 = arr[last_index]
                if tp_2 == "B":  # нашли В
                    break
            else:  # не нашли B
                break
            if m - m - price + price_2 >= 0:  # проверяем, можно ли продать этот В и купить новый модный А
                count_a += 1  # ура, на 1 А теперь больше
                m = m - m - price + price_2  # продаем, покупаем
            else:
                break  # игры кончились
    print(count_a, m)  # ответ
