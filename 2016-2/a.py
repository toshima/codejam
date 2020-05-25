
import sys


def winner(r, p, s):
    while r + p + s > 1:
        r, p, s = (r + s - p) / 2, (p + r - s) / 2, (s + p - r) / 2
    if r == 1 and s == p == 0:
        return 'R'
    elif p == 1 and r == s == 0:
        return 'P'
    elif s == 1 and r == p == 0:
        return 'S'


def solve(w, n):
    if n == 0:
        return w
    if w == 'P':
        a, b = 'PR'
    elif w == 'R':
        a, b = 'RS'
    elif w == 'S':
        a, b = 'SP'

    s1 = solve(a, n-1)
    s2 = solve(b, n-1)

    return ''.join(sorted([s1, s2]))


for tc in range(int(raw_input())):
    n, r, p, s = map(int, raw_input().split())
    w = winner(r, p, s)
    if w is None:
        ans = 'IMPOSSIBLE'
    else:
        ans = solve(w, n)
    sys.stdout.write("Case #{}: {}\n".format(tc+1, ans))

