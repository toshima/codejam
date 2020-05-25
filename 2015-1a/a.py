
import sys


for tc in range(int(raw_input())):
    raw_input()
    counts = map(int, raw_input().split())

    diffs = [max(a-b, 0) for a, b in zip(counts[:-1], counts[1:])]
    maxdiff = max(diffs)
    ans1 = sum(diffs)
    ans2 = sum(min(count, maxdiff) for count in counts[:-1])
    sys.stdout.write("Case #{}: {} {}\n".format(tc+1, ans1, ans2))
