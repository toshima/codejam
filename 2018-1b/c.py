
import sys

read_ints = lambda: map(int, raw_input().split())

num_cases, = read_ints()
for case in range(num_cases):
    m, = read_ints()
    g = []
    for _ in range(m):
        a, b = read_ints()
        g.append((a - 1, b - 1))
    x = [k-1 for k in read_ints()]
    s = search(g)
