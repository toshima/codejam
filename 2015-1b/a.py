
def f(x):
    s = str(x)
    i = len(s) / 2
    a, b = s[:i][::-1], s[i:]
    a = int(a) if a else 0
    b = int(b) if b else 0
    c = int(s) - 10**(len(s)-1)
    assert a + b - 1 <= c
    return min(a + b, c)


def solve(x):
    if x % 10 == 0:
        return solve(x-1) + 1

    ans = 1
    for i in range(1, len(str(x))):
        # print 10**i-1, f(str(10**i-1))
        ans += f(10**i-1) + 1
    # print s, f(s)
    ans += f(x)
    return ans


import sys

for tc in range(int(raw_input())):
    N = int(raw_input())
    sys.stdout.write("Case #{}: {}\n".format(tc+1, solve(N)))
