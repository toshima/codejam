
import sys


def solve(y, x, n):
    if y == 1 or x == 1:
        a = 0
        b = 0
        c = int((x * y - 1) / 2)
    else:
        a = max(0, int(((y-2)*(x-2) + 1) / 2))
        c = 4 if x*y%2 else 2
        b = max(0, x + y - 2 - c)

    print a, b, c

    m = x*y-n
    return (y * (x-1) + x * (y-1)
            - 4 * min(m, a)
            - 3 * min(max(0, m-a), b)
            - 2 * min(max(0, m-a-b), c))


for tc in range(int(raw_input())):
    y, x, n = map(int, raw_input().split())
    sys.stdout.write("Case #{}: {}\n".format(tc+1, solve(y, x, n)))

