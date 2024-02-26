with open(r'files/1_b.txt', 'r') as f:
    n, k = map(int, f.readline().split())
    arr = [int(f.readline()) for _ in range(n)]

arr_mx_left = [-10 ** 9]
for index in range(n):
    arr_mx_left.append(max(arr_mx_left[-1], arr[index]))
arr_mx_right = [-10 ** 9]
for index in range(n - 1, -1, -1):
    arr_mx_right.append(max(arr_mx_right[-1], arr[index]))
arr_mx_right.reverse()
ans = -10 ** 9
for i in range(n - k):
    j = i + k
    mx = max(arr_mx_left[i], arr_mx_right[j + 1])
    ans = max(ans, arr[i] + arr[j] + mx)
print(f'{ans}')
