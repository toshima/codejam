"""

Use binary search. For a given length of time, maximum number of bits that can be handled? Find shortest time which products enough bits

10 11 10
10 12 11
11 12 11


b = 100
10   11   ->12   13
97   98   101    103

"""

import sys

read_ints = lambda: map(int, raw_input().split())

num_cases, = read_ints()
for case in range(num_cases):
    r, b, c = read_ints()
    cashiers = [read_ints() for _ in range(c)]
    lo = 0
    hi = max(m * s + p for m, s, p in cashiers) + 1000
    while lo < hi:
        mid = (lo + hi) / 2
        bits = [min(m, (mid - p) / s) for m, s, p in cashiers]
        f = sum(sorted(bits)[::-1][:r])
        if f >= b:
            hi = mid
        elif f < b:
            lo = mid + 1
    sys.stdout.write("Case #{}: {}\n".format(case, lo))

