
from itertools import combinations
import sys


def product(l):
    p = 1.0
    for x in l:
        p *= x
    return p


def ptie(probs):
    ans = 0.0
    halfs = list(combinations(probs, k/2))
    for yes, no in zip(halfs, halfs[::-1]):
        ans += product(yes) * product(1.0-p for p in no)
    return ans


def brute(probs, k):
    ans = 0.0
    best = None
    for subset in combinations(probs, k):
        p = ptie(subset)
        if p > ans:
            ans = p
            best = subset
    print best
    return ans


def greedy(probs, k):
    probs = sorted(probs)
    ans = 0.0
    for i in range(k+1):
        subset = probs[:i] + (probs[-(k-i):] if i<k else [])
        ans = max(ans, ptie(subset))
    return ans


for tc in range(int(raw_input())):
    _, k = map(int, raw_input().split())
    probs = map(float, raw_input().split())
    # ans = brute(probs, k)
    ans = greedy(probs, k)
    sys.stdout.write("Case #{}: {}\n".format(tc+1, ans))

