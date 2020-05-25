
from math import pi

EPS = 1e-8


def read_ints():
    return map(int, raw_input().split())


def main():
    N, K = read_ints()
    R = []
    H = []
    RH = []
    for i in range(N):
        r, h = read_ints()
        RH.append((i, r, h))

    ans = 0.0
    for i, r, h in RH:
        areas = [2*pi*r1*h1 for j, r1, h1 in RH if i != j and r1 <= r + EPS]
        if len(areas) < K - 1:
            continue
        ans = max(ans, pi*r*r + 2*pi*r*h + sum(sorted(areas)[::-1][:K-1]))
        # print r, h, pi*r*r + sum(sorted(areas)[::-1][:K]), areas
    return ans


import sys
(TC,) = read_ints()
for tc in range(TC):
    ans = main()
    sys.stdout.write("Case #{}: {}\n".format(tc+1, ans))
