from numba import njit, prange

p = [106, 218]
q = [132, 388]
r = [183, 256]
mn = 1000000000

for a_start in p + q + r:
    for a_end in p + q + r:
        if a_end > a_start:
            for x in range(1, 390):
                con = ((not ((q[0] <= x <= q[1]) <= ((p[0] <= x <= p[1]) or (r[0] <= x <= r[1])))) <= (
                        (not (a_start <= x <= a_end)) <= (not (q[0] <= x <= q[1]))))
                # print(a_start, a_end, x, con,
                #       ((not ((q[0] <= x <= q[1]) <= ((p[0] <= x <= p[1]) or (r[0] <= x <= r[1])))),
                #        ((not (a_start <= x <= a_end)) <= (not (q[0] <= x <= q[1])))))
                if con == 0:
                    break
            else:
                mn = min(mn, a_end - a_start)

print(mn)
