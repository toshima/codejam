
import math


EPS = 1e-16


def read_ints():
    return map(int, raw_input().split())

def read_floats():
    return map(float, raw_input().split())


def main():
    N, K = read_ints()
    (U,) = read_floats()
    U = int(10000 * U + 0.5)
    P = [int(10000 * p + 0.5) for p in read_floats()]
    best = sorted(P)[::-1]

    ans = 0
    for k in range(K+1):
    # for k in range(K, K+1):
        lo = 0
        hi = 10001
        while lo < hi:
            # print lo, hi
            mid = (lo + hi) / 2
            total = sum(max(0, mid - p) for p in best[:k])
            if total == U:
                break
            elif total > U:
                hi = mid
            else:
                if lo == mid:
                    break
                lo = mid

        probs = [max(p, mid) for p in best[:k]] + best[k:]
        # print mid, U
        # assert len(probs) == len(P)
        # assert sum(probs) - sum(P) <= U
        # print P, best, probs, mid
        ans = max(ans, calc(probs, K))
    # print ans
    return 10 ** (math.log10(ans) - 4 * N)
    # return ans * 10**(4*N)


def calc(probs, K):
    N = len(probs)
    dp = [[0 for _ in range(N+1)] for _ in range(N)]
    dp[0][0] = 10000-probs[0]
    dp[0][1] = probs[0]
    for i in range(1, N):
        for j in range(N+1):
            dp[i][j] = (10000-probs[i]) * dp[i-1][j]
            if j:
                dp[i][j] += probs[i] * dp[i-1][j-1]
    return sum(dp[N-1][k] for k in range(K, N+1))


def calc2(probs, K):
    import itertools
    ans = 0.0
    q = 1.0
    for x in probs:
        q *= 1-x
    for k in range(K, len(probs)+1):
        for subset in itertools.combinations(probs, k):
            p = q
            for x in subset:
                p *= x / (1-x)
            ans += p
    return ans



import sys
(TC,) = read_ints()
for tc in range(TC):
    ans = main()
    sys.stdout.write("Case #{}: {}\n".format(tc+1, ans))
    # break
