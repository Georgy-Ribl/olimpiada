from math import acos, cos, sqrt, sin


def make_vec(p1, p2):
    return [p2[0] - p1[0], p2[1] - p1[1]]


def vec_len(vec):
    return sqrt(vec[0] ** 2 + vec[1] ** 2)


def is_equal(l):
    return len(set(l)) == 1


n = int(input())
arr = [[float(s) for s in input().split()] for i in range(n)]
tx, ty = -10000, -100000
S_max = 0
p = []
for i1 in range(n):
    for i2 in range(i1 + 1, n):
        for i3 in range(i2 + 1, n):
            for i4 in range(i3 + 1, n):
                for i5 in range(i4 + 1, n):
                    points = [arr[i1], arr[i2], arr[i3], arr[i4], arr[i5]]
                    points_clocwise = [min(points)]
                    greater = [point for point in points if
                               point != points_clocwise[0] and point[1] >= points_clocwise[0][1]]
                    smaller = [point for point in points if
                               point != points_clocwise[0] and point[1] < points_clocwise[0][1]]
                    greater.sort()
                    smaller.sort(reverse=True)
                    points_clocwise += greater + smaller
                    shorts = []
                    angles = []
                    for k in range(len(points_clocwise)):
                        k_min_1 = (k - 1) % len(points_clocwise)
                        k_plus_1 = (k + 1) % len(points_clocwise)
                        vec1 = make_vec(points_clocwise[k], points_clocwise[k_min_1])
                        vec2 = make_vec(points_clocwise[k], points_clocwise[k_plus_1])
                        vec_len_1 = vec_len(vec1)
                        short = round(vec_len_1, 2)
                        vec_len_2 = vec_len(vec2)
                        if vec_len_1 * vec_len_2 == 0:
                            break
                        angle = acos((vec1[0] * vec2[0] + vec1[1] * vec2[1]) / (vec_len_1 * vec_len_2))
                        angles.append(round(angle, 2))
                        shorts.append(short)
                    if len(angles) < 5:
                        continue
                    if not is_equal(angles) or not is_equal(shorts):
                        continue
                    vec1 = make_vec(points_clocwise[2], points_clocwise[0])
                    vec2 = make_vec(points_clocwise[2], points_clocwise[4])
                    alpha = acos((vec1[0] * vec2[0] + vec1[1] * vec2[1]) / (vec_len(vec1) * vec_len(vec2)))
                    l = vec_len(make_vec(points_clocwise[4], points_clocwise[0]))
                    R = 0.5 * l / sin(alpha)
                    S = 1.12257 * R ** 2
                    if S > S_max:
                        S_max = S
                        p = points_clocwise

print("%.2f" % S)
for poit in points_clocwise:
    print(*poit)
