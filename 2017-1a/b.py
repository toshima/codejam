
import sys


def readints():
    return map(int, raw_input().split())


eps = 1e-8


for tc in range(int(raw_input())):
    n, p = readints()
    R = readints()
    Q = [[1.0 * x / r for x in sorted(readints())] for r in R]

    ans = 0
    inds = [0] * n
    while True:
        if any(inds[i] >= p for i in range(n)):
            break

        x = [Q[i][inds[i]] for i in range(n)]
        if max(x) < int(min(x) / 0.9 + eps) * 1.1 + eps:
            for i in range(n):
                inds[i] += 1
            ans += 1
        else:
            i = x.index(min(x))
            inds[i] += 1

    sys.stdout.write("Case #{}: {}\n".format(tc+1, ans))
