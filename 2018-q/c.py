import sys

r = range(450, 550)
rii = lambda: map(int, raw_input().split())
xys = {(x, y) for x in r for y in r}

(num_cases,) = rii()
for _ in range(num_cases):
    (a,) = rii()
    g = {xy: False for xy in xys}
    counts = {xy: 0 for xy in xys}
    seen = False

    while True:
        if not seen:
            ax = ay = 500
            bx = by = 501
            seen = True
        else:
            ax = min(x for x, y in g if g[x, y])
            bx = max(x for x, y in g if g[x, y]) + 1
            ay = min(y for x, y in g if g[x, y])
            by = max(y for x, y in g if g[x, y]) + 1

        axc = sum(g[ax, y] for y in r)
        bxc = sum(g[bx, y] for y in r)
        ayc = sum(g[x, ay] for x in r)
        byc = sum(g[x, by] for x in r)
        minc = min([axc, bxc, ayc, byc])

        if (by - ay) * (bx - ax) < a:
            if axc == minc:
                ax -= 1
            elif bxc == minc:
                bx += 1
            elif ayc == minc:
                ay -= 1
            elif byc == minc:
                by += 1

        if bx - ax < 8:
            ax -= 3
            bx += 3
        if by - ay < 8:
            ay -= 3
            by += 3

        inner = {(x, y) for x in range(ax+1, bx - 1) for y in range(ay+1, by - 1)}
        x, y = min(inner, key=counts.get)
        sys.stdout.write("{} {}\n".format(x, y))
        sys.stdout.flush()

        x, y = rii()
        if x == y == 0:
            break
        elif x == y == -1:
            break

        g[(x, y)] = True
        for dx in [-1, 0, 1]:
            for dy in [-1, 0, 1]:
                counts[(x+dx, y+dy)] += 1
