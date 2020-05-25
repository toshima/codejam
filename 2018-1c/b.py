import sys


read_int = lambda: int(raw_input())


for case in range(int(raw_input())):
    N = int(raw_input())
    used = set()
    seen = {i: 0 for i in range(N)}
    for _ in range(N):
        prefs = map(int, raw_input().split())[1:]
        for x in prefs:
            seen[x] += 1
        unused = [x for x in prefs if x not in used]
        if unused:
            sold = min(unused, key=seen.get)
            used.add(sold)
            print sold
        else:
            print -1
        sys.stdout.flush()


