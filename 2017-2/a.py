
def read_ints():
    return map(int, raw_input().split())


def main():
    N, P = read_ints()
    G = read_ints()
    assert len(G) == N

    x = [sum(g % P == i for g in G) for i in range(P)]

    if P == 2:
        return x[0] + g(x[1], 2)
    elif P == 3:
        a = min(x[1], x[2])
        b = max(x[1], x[2])
        return x[0] + a + g(b - a, 3)
    elif P == 4:
        ans = x[0]

        a = min(x[1], x[3])
        ans += a
        x[1] -= a
        x[3] -= a

        b = min(x[2], (x[1] + x[3]) // 2)
        ans += b
        x[2] -= b
        if x[1] > x[3]:
            x[1] -= 2*b
        else:
            x[3] -= 2*b

        c = x[2] // 2
        ans += c
        x[2] -= 2*c

        d = (x[1] + x[3]) // 4
        ans += d
        if x[1] > x[3]:
            x[1] -= 4*d
        else:
            x[3] -= 4*d

        if x[1] + x[2] + x[3] > 0:
            ans += 1
        return ans

        # b = max(x[1], x[3])
        # c = min(x[2], (b - a) // 2)
        # d = 1 if (b - a) % 2 == 1 or (x[2] - c) % 2 == 1 else 0
        # print a, b, c, d
        # return x[0] + a + c + (x[2] - c) // 2 + d
    else:
        assert False


def g(a, b):
    return (a + b - 1) // b


import sys
(TC,) = read_ints()
for tc in range(TC):
    ans = main()
    sys.stdout.write("Case #{}: {}\n".format(tc+1, ans))
