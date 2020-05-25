import math
import sys


eps = 1e-9

for cs in range(int(raw_input())):
    a = float(raw_input())

    lo, hi = 0.0, math.pi/4.0
    while hi - lo > eps:
        mid = (lo + hi) / 2.0
        res = math.sin(mid) + math.cos(mid)
        if res > a:
            hi = mid
        else:
            lo = mid

    x1, y1 = 0.5*math.cos(mid), 0.5*math.sin(mid)
    x2, y2 = 0.5*math.sin(mid), -0.5*math.cos(mid)
    sys.stdout.write("Case #{}:\n".format(cs+1))
    sys.stdout.write("{} {} 0\n".format(x1, y1))
    sys.stdout.write("{} {} 0\n".format(x2, y2))
    sys.stdout.write("0 0 0.5\n")
