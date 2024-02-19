print('x y z w F')
for x in range(1):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                con = (y and (x or z)) == ((not x or w) and (not w or z))
                if con == True:
                    print(x, y, z, w, con)
