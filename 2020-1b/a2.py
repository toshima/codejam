
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
    n = int(math.log(abs(a) + abs(b), 2) + 1e-9) + 1
    ans = ''
    while a != 0 or b != 0:
        if (a+b) % 2 == 0:
            return 'IMPOSSIBLE'
        if abs(a) > abs(b):
            k = 'E' if a > 0 else 'W'
        else:
            k = 'N' if b > 0 else 'S'

        dx, dy = d[k]
        mult = 2 ** (n-1)

        a -= dx * mult
        b -= dy * mult
        n -= 1
        ans = k + ans
    return ans


t = int(input())
for tc in range(t):
    a, b = map(int, input().split())
    print("Case #{}: {}".format(tc+1, solve(a, b)))

# for a in range(-4, 5):
#     for b in range(-4, 5):
#         print(a, b, solve(a, b), ' ')
#     print()
