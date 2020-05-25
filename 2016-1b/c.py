

def bpm(g1, g2, start):



for tc in range(int(raw_input())):
    g1 = {}
    g2 = {}
    for _ in range(int(raw_input())):
        a = str(raw_input())
        b = str(raw_input())

        if a not in g1:
            g1[a] = []
        g1[a].append(b)

        if b not in g2:
            g2[b] = []
        g2[b].append(a)

