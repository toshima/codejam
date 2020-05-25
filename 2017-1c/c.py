
EPS = 1e-16


def read_ints():
    return map(int, raw_input().split())

def read_floats():
    return map(float, raw_input().split())


def main():
    N, K = read_ints()
    (U,) = read_floats()
    P = read_floats()
    best = sorted(P)[::-1]

    ans = 0.0
    for k in range(K+1):
    # for k in range(K, K+1):
        lo = 0.0
        hi = 1.0
        while lo < hi - EPS:
            mid = 0.5 * (lo + hi)
            total = sum(max(0.0, mid - p) for p in best[:k])
            if total > U:
                hi = mid
            else:
                lo = mid
        print mid

        probs = [max(p, mid) for p in best[:k]] + best[k:]
        assert len(probs) == len(P)
        assert sum(probs) - sum(P) < U + 1e-8
        # print P, best, probs, mid
        ans = max(ans, calc(probs, K))
    return ans


def calc(probs, K):
    N = len(probs)
    dp = [[0.0 for _ in range(N+1)] for _ in range(N)]
    dp[0][0] = 1-probs[0]
    dp[0][1] = probs[0]
    for i in range(1, N):
        for j in range(N+1):
            dp[i][j] = (1-probs[i]) * dp[i-1][j]
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
