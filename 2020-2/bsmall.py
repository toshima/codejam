
def solve(nodes, edges):
    n = len(nodes)
    d = {i+1: x for i, x in enumerate(nodes)}
    d[0] = 0
    return [max(1, abs(d[a] - d[b])) for a, b in edges]


t = int(input())
for tc in range(t):
    c, d = map(int, input().split())
    nodes = [-int(x) for x in input().split()]
    edges = []
    for _ in range(d):
        a, b = map(int, input().split())
        edges.append((a-1, b-1))
    ans = solve(nodes, edges)
    print("Case #{}: {}".format(tc+1, ' '.join(map(str, ans))))
