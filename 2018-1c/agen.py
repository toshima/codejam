import random
import string

N = 2000
L = 10

print 1
print N, L
for _ in range(N):
    print ''.join(random.choice(string.ascii_uppercase) for _ in range(L))

