for tc in range(int(input())):
    _, s = input(), input()
    s = ''.join({"S":"E", "E":"S"}[c] for c in s)
    print("Case #{}: {}".format(tc+1, s))

