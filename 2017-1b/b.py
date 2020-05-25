
import sys


CHECK = ['RG', 'GR', 'VY', 'YV', 'OB', 'BO', 'RY', 'YR', 'YB', 'BY',
         'RB', 'BR']


def solve(N, R, O, Y, G, B, V):
    if 2*R == 2*G == N:
        return "RG" * int(N/2)
    elif 2*R == 2*B == N:
        return "RB" * int(N/2)
    elif 2*R == 2*Y == N:
        return "RY" * int(N/2)
    elif 2*V == 2*Y == N:
        return "VY" * int(N/2)
    elif 2*B == 2*Y == N:
        return "BY" * int(N/2)
    elif 2*B == 2*O == N:
        return "BO" * int(N/2)

    a = R - G
    b = Y - V
    c = B - O
    if R < 2*G or Y < 2*V or B < 2*O or a+b+c < 2*max(a, b, c):
        return "IMPOSSIBLE"

    A1 = []
    B1 = []
    C1 = []
    for _ in range(G):
        A1.append("RGR")
    for _ in range(R-2*G):
        A1.append("R")

    for _ in range(V):
        B1.append("YVY")
    for _ in range(Y-2*V):
        B1.append("Y")

    for _ in range(O):
        C1.append("BOB")
    for _ in range(B-2*O):
        C1.append("B")

    # print len(A1), len(B1), len(C1), a, b, c
    # print "B =", B
    # print A1, B1, C1, a, b, c
    # print "O =", O

    if b == max(a, b, c):
        A1, B1 = B1, A1
        a, b = b, a
    elif c == max(a, b, c):
        A1, C1 = C1, A1
        a, c = c, a
    # print len(A1), len(B1), len(C1)
    # print A1, B1, C1, a, b, c
    assert a >= b and a >= c
    assert len(A1) == a
    assert len(B1) == b
    assert len(C1) == c
    ans = ""
    for i in range(a):
        # print i, a-c, a-c + b+c-a
        if i < a - c:
            s = B1.pop(0)
        elif i < a-c + b+c-a:
            s = B1.pop(0) + C1.pop(0)
        else:
            s = C1.pop(0)
        ans += A1.pop(0) + s

    # print len(ans), N, R, O, Y, G, B, V, ans
    # print len(A1), len(B1), len(C1)

    assert not A1 and not B1 and not C1
    return ans


# def solve_small(N, R, O, Y, G, B, V):
#     (a, ac), (b, bc), (c, cc) = sorted([(R, 'R'), (B, 'B'), (Y, 'Y')])[::-1]
#     if a > b + c:
#         return "IMPOSSIBLE"

#     # print a, b, c, ac, bc, cc

#     ans = ""
#     for i in range(a):
#         ans += ac
#         if i < a - c:
#             ans += bc
#         elif i < a-c + b+c-a:
#             ans += bc + cc
#         else:
#             ans += cc
#     # print ans
#     return ans



def gen_test():
    import random
    print 100
    for _ in range(100):
        x = []
        for _ in range(6):
            x.append(random.randint(0, 100))
        print sum(x), ' '.join(map(str, x))

for tc in range(int(raw_input())):
    N, R, O, Y, G, B, V = map(int, raw_input().split())
    ans = solve(N, R, O, Y, G, B, V)

    if ans != "IMPOSSIBLE":
        assert len(ans) == N
        for a, b in zip(ans, ans[1:] + ans):
            assert a + b in CHECK
        assert ans.count('R') == R
        assert ans.count('O') == O
        assert ans.count('Y') == Y
        assert ans.count('G') == G
        assert ans.count('B') == B
        assert ans.count('V') == V

    sys.stdout.write("Case #{}: {}\n".format(tc+1, ans))
