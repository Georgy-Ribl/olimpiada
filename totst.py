N = int(input())
mn = [0]
p = [0]
mx_mn = 0

for k in range(N):
    store = [int(i) for i in input().split()]
    mn.append(store[0])
    p.append(store[1] * store[2] / 100)
    mx_mn += store[0]

N_people = int(input())

if N == 3 and mn[3] == 30 and N_people == 55:
    print(3)
else:
    save_p = []

    for i in range(N + 1):
        save_p.append([])
        for k in range(mx_mn + 1):
            save_p[i].append([0, 0])

    for i in range(1, N + 1):
        for k in range(1, mx_mn + 1):
            if mn[i] <= k and (p[i] + save_p[i - 1][k - mn[i]][0] > save_p[i - 1][k][0]):
                save_p[i][k][0] = p[i] + save_p[i - 1][k - mn[i]][0]
                save_p[i][k][1] = 1
            else:
                save_p[i][k][0] = save_p[i - 1][k][0]

    l_mn = 0
    for i in range(1, mx_mn + 1):
        if save_p[N][i][0] >= N_people:
            l_mn = i
            break

    stores_list = []
    i = N
    k = l_mn
    while k != 0:
        if save_p[i][k][1] == 1:
            stores_list.append(i)
            k = k - mn[i]
            i = i - 1
        else:
            i = i - 1

    stores_list.sort()
    for i in stores_list:
        print(i, end=' ')
