for tc in range(int(input())):
    n = input()
    a = int(n.replace('4', '3'))
    n = int(n)
    print("Case #{}: {} {}".format(tc+1, a, n-a))

