
import sys

read_ints = lambda: map(int, raw_input().split())

mod1 = lambda x: x - int(x)
eps = 1e-9

num_cases, = read_ints()
for case in range(num_cases):
    n, _ = read_ints()
    c = read_ints()
    c += [0] * n

    if mod1(1.0/n) < 0.5 - eps:
        f = lambda i: mod1(100.0*c[i]/n + 0.5)
    else:
        f = lambda i: -mod1(100.0*c[i]/n)

    k = n - sum(c)
    for _ in range(k):
        best = max(range(len(c)), key=f)
        # print [-mod1(c[i]) for i in range(len(c))]
        c[best] += 1

    # print c, n
    ans = sum(int(round(100.0 * i / n)) for i in c)
    sys.stdout.write("Case #{}: {}\n".format(case+1, ans))

