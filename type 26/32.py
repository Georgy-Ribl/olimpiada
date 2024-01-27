with open(r'files/32.txt', 'r') as f:
    n = int(f.readline())
    nums = sorted([int(i) for i in x.split()] for x in f)
    rmax = 0
    for i in range(1, n):
        r, m = nums[i - 1]
        if r == nums[i][0] and nums[i][1] - m == 14:
            if r > rmax: rmax, mmin = r, m
    print(rmax, mmin + 1)
