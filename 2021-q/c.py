
def solve(n, cost):
    nums = list(range(1, n+1))
    for i in range(n-2, -1, -1):
        c = min(n-i, cost - i)
        if c < 1:
            return "IMPOSSIBLE"
        nums[i:i+c] = nums[i:i+c][::-1]
        cost -= c
    if cost:
        return "IMPOSSIBLE"
    return " ".join(map(str, nums))


TC = int(input())
for tc in range(TC):
    n, cost = map(int, input().split())
    ans = solve(n, cost)
    print("Case #{}: {}".format(tc+1, ans))

