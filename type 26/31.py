with open(r'files/31.txt') as f:
    n = int(f.readline())
    L = []
    w0 = 1634515200
    w1 = w0 + 7 * 24 * 3600
    for i in f:
        st, en = [int(x) for x in i.split()]
        if en == 0: en = w1
        if st >= w1 or en <= w0: continue
        L.extend([(max(st, w0), 1), (min(en, w1), -1)])
    L.sort()
    mxk = k = 0
    for t, dk in L:
        k += dk
        if k > mxk: mxk, dt = k, 0
        if k - dk == mxk: dt += t - t0
        t0 = t
    print(mxk, dt)
