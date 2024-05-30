print('x y z w F')
for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                r = not w
                con = (x <= r) and (y <= x) and z
                if con:
                    print(x, y, z, w, 1)
