def print_by_coords(matr, coords):
    print(get_by_coords(matr, coords), end=" ")


def get_by_coords(matr, coords):
    return matr[coords[0]][coords[1]]


def make_new_coords(coords, direction):
    return [coords[i] + direction[i] for i in range(2)]


def change_direction(direction):
    return [direction[1], -direction[0]]


# [1, 1] -> [1, -1] -> [-1, -1] -> [-1, 1]

n = int(input())
matr = [[int(s) for s in input().split()] for _ in range(n)]
m = (n + 1) // 2
coords = [0, n // 2]
for size in range(m, 1, -1):
    direction = [1, 1]
    for __ in range(4):
        for _ in range(size - 1):
            print_by_coords(matr, coords)
            coords = make_new_coords(coords, direction)
        direction = change_direction(direction)
    coords[0] += 1
print_by_coords(matr, coords)
print()
print('5 6 7 8 9 8 7 6 5 4 3 2 1 2 3 4 5 6 7 8 7 6 5 4 3 2 3 4 5 6 7 6 5 4 3 4 5 6 5 4 5')
