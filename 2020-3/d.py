
import math


def solve(l, d):
    l = [(y+x, y-x) for x, y in l]
    a, b = l[:2]
    inter0 = max(0, 2*d - abs(a[0] - b[0]))
    inter1 = max(0, 2*d - abs(a[1] - b[1]))
    inter2 = max(0, 2*inter0 - 2*d)
    inter3 = max(0, 2*inter1 - 2*d)
    inter4 = max(0, 2*inter2 - inter0)
    inter5 = max(0, 2*inter3 - inter1)

    num = 6*inter0*inter1 - 2*inter2*inter3 + inter4*inter5
    den = 16*d*d - 2*inter0*inter1
    h = math.gcd(num, den)
    num, den = num//h, den//h
    # print(inter0, inter1)
    # print(inter2, inter3)
    # print(inter4, inter5)
    return num, den



T = int(input())
for tc in range(T):
    n, d = map(int, input().split())
    l = []
    for _ in range(n):
        x, y = map(int, input().split())
        l.append((x, y))
    num, den = solve(l, d)
    print("Case #{}: {} {}".format(tc+1, num, den))

