
def solve(cj, jc, s):
    s = s.replace("?", "")
    ans = 0
    for i in range(len(s)):
        if s[i:i+2] == "CJ":
            ans += cj
        elif s[i:i+2] == "JC":
            ans += jc
    return ans

TC = int(input())
for tc in range(TC):
    cj, jc, s = input().split()
    ans = solve(int(cj), int(jc), s)
    print("Case #{}: {}".format(tc+1, ans))

