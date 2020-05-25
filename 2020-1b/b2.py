from __future__ import print_function
import sys

def eprint(*args, **kwargs):
    print(*args, file=sys.stderr, **kwargs)


t, a, b = map(int, input().split())

n = 10**9

for _ in range(t):
    x = y = 0
    while True:
        print(x-n, -51)
        sys.stdout.flush()
        if input() == 'HIT':
            break
        x += 1

    while True:
        print(-51, y-n)
        sys.stdout.flush()
        if input() == 'HIT':
            break
        y += 1

    # eprint(x, y, a)
    print(x-1+a-n, y-1+a-n)
    sys.stdout.flush()
    res = input()
    assert res == 'CENTER'

