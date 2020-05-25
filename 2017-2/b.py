
from collections import defaultdict


def read_ints():
    return map(int, raw_input().split())


def main():
    N, C, M = read_ints()
    d = defaultdict(int)
    for _ in range(M):
        P, B = read_ints()
        d[(B, P)] += 1

    rides = 0
    promotions = 0
    while d:
        # print d
        count = defaultdict(int)
        for c, _ in d:
            count[c] += 1
        maxcount = max(count)

        g = [(a, b, cap) for (a, b), cap in d.items()]
        flow, edges = maxmatch(g)

        rides += 1
        for a, b in edges:
            d[(a, b)] -= 1
            assert d[(a, b)] >= 0
            if d[(a, b)] == 0:
                del d[(a, b)]

        counta = defaultdict(int)
        countb = defaultdict(int)
        for a, b in edges:
            counta[a] += 1
            countb[b] += 1
        usedcust = {a for a, b in edges}
        freeseat = range(1, N+1)
        for _, b in edges:
            freeseat.remove(b)
        for a, b in sorted(d.keys(), key=lambda (a, b): (counta[a]+ countb[b]))[::-1]:
            # for c in sorted(count.keys(), key=count.get)[::-1]:
            if not freeseat:
                break
            if a not in usedcust and freeseat[0] < b:
                promotions += 1
                usedcust.add(a)
                for u in freeseat[:][::-1]:
                    # print u
                    if u < b:
                        freeseat.remove(u)
                        break
                d[(a, b)] -= 1
                assert d[(a, b)] >= 0
                if d[(a, b)] == 0:
                    del d[(a, b)]
                # break

        # print
    return rides, promotions


def maxmatch(edges):
    source = object()
    sink = object()
    left = object()
    right = object()
    g = [((left, a), (right, b), cap) for a, b, cap in edges]
    for node in {a for a, _, _ in edges}:
        g.append((source, (left, node), 1))
    for node in {b for _, b, _ in edges}:
        g.append(((right, node), sink, 1))
    matches, new_edges = maxflow(g, source, sink)
    new_edges = [(a[1], b[1]) for (a, b, flow) in new_edges if flow > 0
                 and a != source and b != sink]
    return matches, new_edges


def maxflow(edges, source, sink):
    graph = {}

    for a, b, capacity in edges:
        if a not in graph:
            graph[a] = {}
        if b not in graph[a]:
            graph[a][b] = 0

        if b not in graph:
            graph[b] = {}
        if a not in graph[b]:
            graph[b][a] = 0

        graph[a][b] += capacity

    flow = 0
    while True:
        parent = {source: None}
        q = [source]
        found = False

        while q:
            a = q.pop(0)
            if a == sink:
                found = True
                break
            for b, cap in graph[a].items():
                if b not in parent and cap > 0:
                    parent[b] = a
                    q.append(b)

        if not found:
            break

        path = []
        node = sink
        while node != source:
            path.append(node)
            node = parent[node]

        cap = min(graph[parent[b]][b] for b in path)
        flow += cap
        for b in path:
            a = parent[b]
            graph[a][b] -= cap
            graph[b][a] += cap

    new_edges = [(a, b, cap-graph[a][b]) for a, b, cap in edges]
    return flow, new_edges


import sys
(TC,) = read_ints()
for tc in range(TC):
    a, b = main()
    sys.stdout.write("Case #{}: {} {}\n".format(tc+1, a, b))
