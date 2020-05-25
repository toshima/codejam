
import sys

read_ints = lambda: map(int, raw_input().split())


def check(signs, k):
    if k == 0:
        return 1
    count = 0
    for i in range(len(signs) - k + 1):
        m, n = signs[i]
        s1 = {a for a, b in signs[i:i+k] if b != n}
        s2 = {b for a, b in signs[i:i+k] if a != m}
        if len(s1) <= 1 or len(s2) <= 1:
            count += 1
        # print signs[i:i+k], s1, s2
    return count

num_cases, = read_ints()
for case in range(num_cases):
    s, = read_ints()
    signs = []
    for _ in range(s):
        d, a, b = read_ints()
        signs.append((d+a, d-b))
    
    # print signs
    lo = 0
    hi = s
    while lo < hi:
        mid = (lo + hi + 1) / 2
        f = check(signs, mid)
        # print mid, f
        if f <= 0:
            hi = mid - 1
        else:
            lo = mid
    sys.stdout.write("Case #{}: {} {}\n".format(case+1, hi, check(signs, hi)))

