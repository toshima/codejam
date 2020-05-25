
def read_ints():
    return map(int, raw_input().split())


import sys
(TC,) = read_ints()
for tc in range(TC):
    ans = main()
    sys.stdout.write("Case #{}: {}\n".format(tc+1, ans))
