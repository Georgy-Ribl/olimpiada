arr = [int(input()) for i in range(6)]
time = 24 * 60
r = max([arr[i] for i in range(5)]) + 1
r += arr[-1]
print(time // r)
