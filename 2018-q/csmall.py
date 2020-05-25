import sys

rii = lambda: map(int, raw_input().split())
r = range(450, 550)
xys = {(x, y) for x in r for y in r}

(num_cases,) = rii()
for _ in range(num_cases):
    (a,) = rii()
    g = {xy: False for xy in xys}
    counts = {xy: 0 for xy in xys}
    ax = ay = 495
    bx = by = 505

    while True:
        inner = {(x, y) for x in range(ax+1, bx-1) for y in range(ay+1, by-1)}
        x, y = min(inner, key=counts.get)
        sys.stdout.write("{} {}\n".format(x, y))
        sys.stdout.flush()

        x, y = rii()
        if x == y == 0:
            break
        elif x == y == -1:
            sys.exit()

        g[(x, y)] = True
        for dx in [-1, 0, 1]:
            for dy in [-1, 0, 1]:
                counts[(x+dx, y+dy)] += 1

