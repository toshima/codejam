letters = [chr(ord('A')+i) for i in range(26)]

def gcd(a, b):
    if a > b:
        return gcd(b, a)
    if not a:
        return b
    return gcd(b%a, a)

for tc in range(int(input())):
    input()
    products = list(map(int, input().split()))

    pivot = 0
    while products[pivot] == products[pivot+1]:
        pivot += 1

    primes = [products[pivot] // gcd(products[pivot], products[pivot+1])]
    for x in products[:pivot][::-1]:
        assert(x % primes[0] == 0)
        primes = [x // primes[0]] + primes
    for x in products[pivot:]:
        assert(x % primes[-1] == 0)
        primes.append(x // primes[-1])

    d = dict(zip(sorted(set(primes)), letters))
    assert(len(set(primes)) == 26)
    ans = ''.join(d[prime] for prime in primes)
    print("Case #{}: {}".format(tc+1, ans))

