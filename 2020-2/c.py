
import math


def solve(l):
    n = len(l)
    seen = set()
    lines = {}
    for j in range(n):
        for i in range(j):
            if (i, j) in seen:
                continue
            x1, y1 = l[i]
            x2, y2 = l[j]
            dx = x2 - x1
            dy = y2 - y1
            line = [i, j]
            for k in range(n):
                if k not in {i, j}:
                    x3, y3 = l[k]
                    dx2 = x3 - x1
                    dy2 = y3 - y1
                    if dx * dy2 == dy * dx2:
                        line.append(k)
            for a in line:
                for b in line:
                    seen.add((a, b))

            gcd = math.gcd(dx, dy)
            dx //= gcd
            dy //= gcd
            if dx < 0:
                dx = -dx
                dy = -dy
            if dx == 0:
                dy = abs(dy)
            grad = dx, dy
            if grad not in lines:
                lines[grad] = []
            lines[grad].append(len(line))

    ans = 1
    for counts in lines.values():
        c = sum(counts)
        if sum(n % 2 for n in counts) % 2 == 1:
            c -= 1
            c = max(0, c)
        c += 2
        c = min(c, n)
        ans = max(ans, c)
    return ans



t = int(input())
for tc in range(t):
    l = []
    for _ in range(int(input())):
        x, y = map(int, input().split())
        l.append((x, y))
    print("Case #{}: {}".format(tc+1, solve(l)))
