
from collections import deque


def solve(nodes, edges):
    n = len(nodes)
    orderq = deque()
    latq =deque()
    orderq.appendleft(0)

    nodes = dict(enumerate(nodes))

    adj = [[] for _ in range(n)]
    for a, b in edges:
        adj[a].append(b)
        adj[b].append(a)

    count = 0
    lat = 1
    latencies = {0: 0}

    while orderq or latq:
        print(count, orderq, latq, nodes)
        lat += 1
        count2 = count
        while orderq and -nodes[orderq[0]] == count:
            x = orderq.popleft()
            count2 += 1
            latencies[x] = lat
            for y in adj[x]:
                if y in latencies:
                    continue
                if nodes[y] > 0:
                    latq.append(y)
                else:
                    orderq.append(y)
        count = count2

        if latq:
            x = latq.popleft()
            lat = nodes[x]
            count += 1
            latencies[x] = lat
            for y in adj[x]:
                if y in latencies:
                    continue
                if nodes[y] > 0:
                    latq.append(y)
                else:
                    orderq.append(y)

    return [max(1, abs(latencies[a] - latencies[b])) for a, b in edges]


t = int(input())
for tc in range(t):
    c, d = map(int, input().split())
    nodes = [0] + [int(x) for x in input().split()]
    edges = []
    for _ in range(d):
        a, b = map(int, input().split())
        edges.append((a-1, b-1))
    ans = solve(nodes, edges)
    print("Case #{}: {}".format(tc+1, ' '.join(map(str, ans))))
