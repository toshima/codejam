import sys


t, a, b = map(int, input().split())

n = 2 * 10**9

for _ in range(t):
    done = False
    for i in range(-5, 6):
        for j in range(-5, 6):
            print(i, j)
            sys.stdout.flush()
            res = input()
            if res == 'CENTER':
                done = True
                break
        if done:
            break
        
