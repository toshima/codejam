
def solve(r, s):
    from functools import lru_cache

    @lru_cache(None)
    def f(t):
        found = False
        for i in range(len(t))[::-1]:
            if t[i] % r != i // s:
                found = True
                break
        if not found:
            return t
        for j in range(i):
            if t[j] % r == t[i] % r:
                break
        return 




t = int(input())
for tc in range(t):
    r, s = map(int, input().split())
    print("Case #{}: {} {}".format(tc+1, solve(r, s)))
