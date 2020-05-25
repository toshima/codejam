
import sys


for tc in range(int(raw_input())):
    R, C = map(int, raw_input().split())
    grid = [list(raw_input()) for _ in range(R)]

    for row in grid:
        prev = None
        for i in range(len(row)) + range(len(row))[::-1]:
            if row[i] != '?':
                prev = row[i]
            elif row[i] == '?' and prev is not None:
                row[i] = prev

    prev = None
    for i in range(len(grid)) + range(len(grid))[::-1]:
        empty = all(x == '?' for x in grid[i])
        if not empty:
            prev = grid[i]
        elif empty and prev is not None:
            grid[i] = prev

    sys.stdout.write("Case #{}:\n".format(tc+1))
    for row in grid:
        sys.stdout.write(''.join(row) + "\n")
        assert '?' not in row
