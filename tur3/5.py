def make_vector(point1, point2):
    return point2[0] - point1[0], point2[1] - point1[1]


def get_area(vector1, vector2):
    return vector1[0] * vector2[1] - vector1[1] * vector2[0]


def get_area_by_points(point1, point2, point3):
    vector1 = make_vector(point2, point3)
    vector2 = make_vector(point2, point1)
    return get_area(vector1, vector2)


def is_anti_clockwize(point1, point2, point3):
    return get_area_by_points(point1, point2, point3) > 0


def area_coeff(area1, area2):
    if area2 == 0:
        return 0
    return area1 / area2


def check_if_are_on_diff_sides_of_line(line_point1, line_point2, point1, point2):
    areas = []
    for point in (point1, point2):
        vector1 = make_vector(point, line_point1)
        vector2 = make_vector(point, line_point2)
        areas.append(get_area(vector1, vector2))
    return area_coeff(areas[0], areas[1]) < 0


def check_is_unique(*points):
    return len(points) == len(set(points))


def get_anticlockwize(points):
    min_x, top_y = points[0]
    for x, y in points:
        if y > top_y:
            top_y = y
            min_x = x
        elif y == top_y and x < min_x:
            top_y = y
            min_x = x
    top_y_min_x = (min_x, top_y)
    rem_points = [el for el in points if el != top_y_min_x]
    anti_clockwize = []
    search_anti = None
    for point in rem_points:
        for point1 in rem_points:
            for point2 in rem_points:
                if check_is_unique(point, point1, point2):
                    if check_if_are_on_diff_sides_of_line(top_y_min_x, point, point1, point2):
                        search_anti = point
                        if is_anti_clockwize(top_y_min_x, point1, search_anti):
                            anti_clockwize = [top_y_min_x, point1, search_anti, point2]
                        elif is_anti_clockwize(top_y_min_x, point2, search_anti):
                            anti_clockwize = [top_y_min_x, point2, search_anti, point1]
    return anti_clockwize


def check_convexity(anti_clockwize):
    firt_seq = [anti_clockwize[0], anti_clockwize[2], anti_clockwize[1], anti_clockwize[3]]
    sec_seq = [anti_clockwize[1], anti_clockwize[3], anti_clockwize[0], anti_clockwize[2]]
    return check_if_are_on_diff_sides_of_line(*firt_seq) and check_if_are_on_diff_sides_of_line(*sec_seq)


def check_equality_and_get_size(anti_clockwize, data):
    points = anti_clockwize + [anti_clockwize[0]]
    counters = []
    set_points = set(data)
    for i in range(len(points) - 1):
        p1 = points[i]
        p2 = points[i + 1]
        other_point = points[(i + 3) % 5]
        counter = 0
        for point in data:
            if check_if_are_on_diff_sides_of_line(p1, p2, other_point, point):
                counter += 1
                set_points.discard(point)
        counters.append(counter)
    return min(counters) == max(counters), len(set_points)


def check(points, data):
    size = None
    isTrue = check_is_unique(*points)
    anti_clockwize = get_anticlockwize(points)
    isTrue = isTrue and len(anti_clockwize) > 0
    if isTrue:
        isTrue = isTrue and check_convexity(anti_clockwize)
        is_equal, size = check_equality_and_get_size(anti_clockwize, data)
        isTrue = isTrue and is_equal
    return isTrue, size, anti_clockwize


def get_all_variants(points, ind, data, best_points):
    if len(points) == 4:
        isTrue, size, anti_clockwize = check(points, data)
        best_size, b_points = best_points
        if isTrue:
            if size > best_size:
                best_points[0] = size
                best_points[1] = anti_clockwize
        return
    for i in range(ind, len(data)):
        points.append(data[i])
        get_all_variants(points, i + 1, data, best_points)
        points.pop()


def read_data():
    N = int(input())
    data = []
    for i in range(N):
        data.append(tuple(map(float, input().split())))
    return data


data = read_data()
best_points = [-1, []]
get_all_variants([], 0, data, best_points)
if best_points[0] == -1:
    print(0)
    data.sort()
    for el in data:
        print("%.2f %.2f" % el)
else:
    for point in best_points[1]:
        print("%.2f %.2f" % point)
