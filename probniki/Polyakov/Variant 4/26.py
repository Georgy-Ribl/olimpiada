array = []
with open("input.txt", "r") as file:
    N = int(file.readline())
    for line in file:
        st, end = map(int, line.split())
        array.append((st, 1))
        array.append((end, -1))
array.sort()
max_cnt = 0
num_of_intervals = 0
counter = 0
for time, flag in array:
    counter += flag
    if counter > max_cnt:
        max_cnt = counter
        num_of_intervals = 1
    elif counter == max_cnt:
        num_of_intervals += 1
print(num_of_intervals, max_cnt)
