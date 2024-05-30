with open(r'files/26.txt', 'r') as file:
    m, n = map(int, file.readline().split())
    arr = [[int(s) for s in file.readline().split()] for _ in range(n)]
arr_time = []
for i in range(n):
    arr_time.append([arr[i][0], 1])
    arr_time.append([arr[i][1], -1])
print(arr_time)
arr_time.sort()
print(arr_time)
'''
Ввожу с(второй элемент) и сравниваю с максимальным с, максимизируя
'''
# minutes = 0
# kol_vo = 0
# k = 0
# mx, mn = 0, 100000
# ls = arr[0][1]
# for i in range(1, n):
#     if arr[i][0] <= ls <= arr[i][1]:
#         k += 1
#         mx = max(mx, arr[i][1])
#         mn = min(mn, arr[i][0])
#     else:
#         kol_vo = max(kol_vo, k)
#         k = 0
#         minutes = max(minutes, mx - mn)
# print(kol_vo)
# print(minutes)
