
def solve(x):
    i = x.index(min(x))
    lo, hi = 0, x[i]
    x = x[i+1:] + x[:i+1]
    ans = 0
    for d in x:
        lo = min(lo, d)
        hi = min(hi, d)
        if lo == hi:
            ans += 1
            lo, hi = 0, d
        else:
            lo, hi = d - hi, d - lo
    if not ans and len(x) % 2 == 0 and sum(x) != sum(x[::2]) * 2:
        ans = 1
    return ans + len(x)


T = int(input())
for tc in range(T):
    k, _ = map(int, input().split())
    x = list(map(int, input().split()))
    input()
    dx = [a - b for a, b in zip(x[1:], x)]
    dx.append(x[0] + k - x[-1])
    ans = solve(dx)
    print("Case #{}: {}".format(tc+1, ans))

