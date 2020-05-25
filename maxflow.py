
def maxmatch(edges):
    source = object()
    sink = object()
    g = [(a, b, 1) for a, b in edges]
    for node in {a for a, _ in edges}:
        g.append((source, node, 1))
    for node in {b for _, b in edges}:
        g.append((node, sink, 1))
    matches, new_edges = maxflow(g, source, sink)
    new_edges = [(a, b) for (a, b, flow) in new_edges if flow > 0
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

