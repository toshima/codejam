import sys

rii = lambda: map(int, raw_input().split())

for cs in range(rii()[0]):
    rii()
    l = rii()
    a = sorted(l)
    l[::2] = sorted(l[::2])
    l[1::2] = sorted(l[1::2])
    ans = "OK"
    for i in range(len(l)):
        if a[i] != l[i]:
            ans = i
            break
    sys.stdout.write("Case #{}: {}\n".format(cs+1, ans))
