from math import acos, sqrt, cos

# points_x_y = [[int(s) for s in input().split()] for _ in range(3)]
points_x_y = [[-5, -3], [-2, 1], [2, 0]]


# Угол между точками, расстояние, площадь образованного треугольника, точки пересечения двух отрезков
def vectorize(point_1, point_2):
    return [point_2[0] - point_1[0], point_2[1] - point_1[1]]


def get_vector_module(vector):
    return sqrt(vector[0] ** 2 + vector[1] ** 2)


def angle(vector1, vector2):
    angle = acos(
        (vector1[0] * vector2[0] + vector1[1] * vector2[1]) / (get_vector_module(vector1) * get_vector_module(vector2)))
    return angle


def three_points_angle(point1, point2, point3):
    vec1 = vectorize(point2, point1)
    vec2 = vectorize(point2, point3)

    return angle(vec1, vec2)


def distance(point1, point2):
    distance = get_vector_module(vectorize(point1, point2))
    return distance


def formula_gerona(point1, point2, point3):
    a = distance(point1, point2)
    b = distance(point1, point3)
    c = distance(point2, point3)
    p = (a + b + c) / 2
    S = sqrt(p * sqrt(p - a) * sqrt(p - b) * sqrt(p - c))
    return S


def is_n_angle_regular(points):
    dist = [distance(points[i], points[i + 1]) for i in range(len(points) - 1)]
    dist.append(distance(points[0], points[-1]))
    k1 = dist[0]
    for elem in dist:
        if elem != k1:
            return False
    return True


def sort_points(points: list[list]) -> list[list]:
    sorted_points = []
    for point in points:
        sorted_points.append([point[0], -point[1]])
    sorted_points.sort()
    print(sorted_points)
    return sorted_points


print(f'№1: {three_points_angle(*points_x_y[0:3])}')
print(f'№2: {distance(*points_x_y[0:2])}')
print(f'№3: {formula_gerona(*points_x_y[0:3])}')
n = int(input())
points_x_y = [[int(s) for s in input().split()] for _ in range(n)]
print(f'№4: {is_n_angle_regular(points_x_y)}')
print(f'№5: {is_n_angle_regular(sort_points(points_x_y))}')
