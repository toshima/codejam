
import math

def solve(l, r):
    l0, r0 = l, r
    n = int(math.sqrt(abs(l-r)*2 + 0.25) - 0.5 + 1e-9)

    if l >= r:
        l -= (n * (n+1)) // 2
    else:
        r -= (n * (n+1)) // 2

    if r > l:
        n += 1
        r -= n

    if n % 2 == 0:
        m = n // 2
        a = int(math.sqrt(l + m*m + 1e-9)) - m
        b = int(math.sqrt(r + m*(m+1) + 0.25) - 0.5 + 1e-9) - m
    else:
        m = n // 2
        a = int(math.sqrt(l + m*(m+1) + 0.25) - 0.5 + 1e-9) - m
        m = (n+1) // 2
        b = int(math.sqrt(r + m*m + 1e-9)) - m

    if b < a:
        a = b+1
    else:
        b = a

    if n % 2 == 0:
        m = n // 2
        l -= (a+m)**2 - m*m
        r -= (b+m)*(b+m+1) - m*(m+1)
    else:
        m = n // 2
        l -= (a+m)*(a+m+1) - m*(m+1)
        m = (n+1) // 2
        r -= (b+m)**2 - m*m
    n += a + b

    return n, l, r



t = int(input())
for tc in range(t):
    l, r = map(int, input().split())
    n, l, r = solve(l, r)
    print("Case #{}: {} {} {}".format(tc+1, n, l, r))
