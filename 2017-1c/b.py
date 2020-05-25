
from math import pi

EPS = 1e-8


def read_ints():
    return map(int, raw_input().split())


def main():
    C, J = read_ints()
    X = []
    for _ in range(C):
        a, b = read_ints()
        X.append((a, b, False))
    for _ in range(J):
        a, b = read_ints()
        X.append((a, b, True))
    X = sorted(X)

    t1 = t2 = 0
    for a, b, c in X:
        if c:
            t2 += b - a
        else:
            t1 += b - a

    changes = 0
    free = 0
    gaps1 = []
    gaps2 = []
    for (a1, b1, c1), (a2, b2, c2) in zip(X, X[1:] + X):
        gap = (a2 - b1 + 24*60) % (24*60)
        if not c1 and not c2:
            gaps1.append(gap)
        elif c1 and c2:
            gaps2.append(gap)
        else:
            free += gap
        if c1 != c2:
            changes += 1

    assert changes % 2 == 0
    gaps1 = sorted(gaps1)[::-1]
    gaps2 = sorted(gaps2)[::-1]

    # print changes, free, gaps1, gaps2

    ans = None
    for i1 in range(len(gaps1) + 1):
        for i2 in range(len(gaps2) + 1):
            lo1 = t1 + sum(gaps1[i1:])
            hi1 = t1 + sum(gaps1) + sum(gaps2[:i2])
            lo2 = t2 + sum(gaps2[i2:])
            hi2 = t2 + sum(gaps2) + sum(gaps1[:i1])
            assert hi1 + lo2 + free == 1440
            assert hi2 + lo1 + free == 1440
            # print lo1, hi1, lo2, hi2
            # print max(0, lo1 - 720),max(0, lo2 - 720),max(0, 720 - hi1),max(0, 720 - hi2)
            if max(0, lo1 - 720) + max(0, lo2 - 720) + max(0, 720 - hi1) + max(0, 720 - hi2) <= free:
                ans1 = changes + 2 * (i1 + i2)
                ans = ans1 if ans is None else min(ans, ans1)
                # if ans1 == 4: print i1, i2, gaps1[:i1], gaps2[:i2], x1, x2
    return ans



import sys
(TC,) = read_ints()
for tc in range(TC):
    ans = main()
    sys.stdout.write("Case #{}: {}\n".format(tc+1, ans))
