
import sys


for tc in range(int(raw_input())):
    D, N = map(int, raw_input().split())
    t = 0
    for _ in range(N):
        K, S = map(int, raw_input().split())
        t = max(t, float(D - K)/float(S))
    sys.stdout.write("Case #{}: {}\n".format(tc+1, float(D)/float(t)))
