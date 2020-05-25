
d = {
    'S': [0, -1],
    'N': [0, 1],
    'W': [-1, 0],
    'E': [1, 0],
}


def solve(a, b):
    if a == b == 0:
        return ''
    import math
    limit = int(math.log(abs(a) + abs(b), 2) + 1e-9) + 1
    limit = 8
    q = []
    q.append((0, 0, ''))
    seen = set()
    while q:
        x, y, s = q.pop(0)
        if x == a and y == b:
            return s
        if len(s) > limit:
            continue
        if (x, y) in seen:
            continue
        seen.add((x, y))
        for k in d:
            dx, dy = d[k]
            mult = 2 ** len(s)
            q.append((x+dx*mult, y+dy*mult, s + k))
    return 'IMPOSSIBLE'


t = int(input())
for tc in range(t):
    a, b = map(int, input().split())
    print("Case #{}: {}".format(tc+1, solve(a, b)))

#     for a in range(-4, 5):
#         for b in range(-4, 5):
#             print(a, b, solve(a, b), ' ')
#         print()
