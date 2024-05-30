print('x y z w F')
for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                con = (y <= x) and not (z) and w
                if con:
                    print(x, y, z, w, con)
