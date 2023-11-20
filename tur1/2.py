x = int(input())
y = int(input())

wall_area = 2 * x * y + 4 * (x - 2) + 4 * y
door_area = 2

long_wall = max(x, y)

window_area = 0

long_wall_windows = round((long_wall - 2) / 3)
window_area += long_wall_windows * 2

total_area = wall_area - door_area - window_area
total_trees = total_area // 2

print(total_trees)
